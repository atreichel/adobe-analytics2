
from datetime import datetime
from datetime import timedelta
from urllib.parse import urlencode
import itertools as it

import numpy as np

import jwt
import requests as req

from pyanalytics2.models.ranked_request import RankedRequest
from pyanalytics2.models.analytics_segment_response_item import AnalyticsSegmentResponseItem
from pyanalytics2.models.analytics_user import AnalyticsUser
from pyanalytics2.segments import Segments
from pyanalytics2.users import Users
from pyanalytics2.models.row import Row
from pyanalytics2.models.ranked_column_meta_data import RankedColumnMetaData
from pyanalytics2.models.report_dimension import ReportDimension
from pyanalytics2.models.ranked_column_error import RankedColumnError
from pyanalytics2.report import Report


class ReportSuite(object):
    '''
        TODO descr, summaryData


        Parameters
        ----------
        client_id : str
            Client ID or API-Key.
        org_id : str
            Organization ID.
        proxy : dict
            Protocol, address pair for connection through a proxy server:
            E.g. {'https':'https://<address>:<port>'}
        access_token : str
            Access token from Adobe's IMS.
        client_id : str
            Client ID or API-Key.
        glob_company_id : str
            Global company ID.
        proxy : dict
            Protocol, address pair for connection through a proxy server:
            E.g. {'https':'https://<address>:<pair>'}
        access_token : str
            Access token from Adobe's IMS.
    '''
    IMS_HOST = 'https://ims-na1.adobelogin.com'
    JWT_URL = '{}/ims/exchange/jwt'.format(IMS_HOST)
    BASE_API_URL = 'https://analytics.adobe.io/api'
    DISCOVERY_URL = 'https://analytics.adobe.io/discovery/me'
    def __init__(self, client_id, secret, tech_acc_email, tech_acc_id, org_id,  private_key_path,
                 report_suite_id=None, scope='ent_analytics_bulk_ingest_sdk', proxy=None, *args, **kwargs):
        self._proxy = proxy
        self._client_id = client_id
        self._secret = secret
        self._tech_acc_email = tech_acc_email
        self._tech_acc_id = tech_acc_id
        self._org_id = org_id
        self._priv_key_path = private_key_path
        self._scope = scope
        self._glob_company_id = None
        self._report_suite_id = report_suite_id
        self._last_update = None
        self._expiry_date = None
        self._jwt_token = None
        self._access_token = None


    def init(self, decode=True):
        # get jwt and access token
        jwt_token = self.create_jwt_token(decode=decode)
        access_token, expires_in = self.request_auth_token(jwt_token)

        if expires_in==0:
            return False

        self._jwt_token = jwt_token
        self._expiry_date = self._last_update + timedelta(seconds=expires_in)
        self._access_token = access_token

        # validate access token and get glob company id of necessary
        dscvry_res = self.discovery()
        if len(dscvry_res)==0:
            return False
        self._glob_company_id = dscvry_res['imsOrgs'][0]['companies'][0]['globalCompanyId']
        return True



    def discovery(self):
        '''
            Get basic information about the organization.

            Parameters
            ----------

            Returns
            -------
           discovery : dict
                Basic information about the organization.
        '''
        status_code, resp = self._make_request('GET', ReportSuite.DISCOVERY_URL, {}, use_org_id=True)
        if status_code==200:
            return resp
        return {}



    def request_auth_token(self, jwt_token):
        '''
            Generate an access token from a JWT-Token.
        '''
        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Cache-Control'] = 'no-cache'

        token_payload = {}
        token_payload['client_id'] = self._client_id
        token_payload['client_secret'] = self._secret
        token_payload['jwt_token'] = jwt_token
        data = urlencode(token_payload)

        if self._proxy is None:
            r = req.post(ReportSuite.JWT_URL, data=data, headers=headers)
        else:
            r = req.post(ReportSuite.JWT_URL, data=data, headers=headers, proxies=self._proxy)
        if r.status_code!=200:
            return '', 0

        response = r.json()
        access_token = response['access_token']
        expires_in = response['expires_in'] # in ms
        return access_token, int(expires_in/1000)



    def create_jwt_token(self, decode=True):
        '''
            Create a JWT-Token.
        '''
        self._last_update = datetime.now()
        jwt_payload = {}
        # expiration
        jwt_payload['exp'] = int((self._last_update + timedelta(hours=24)).timestamp())
        # issuer
        jwt_payload['iss'] = self._org_id
        # subject
        jwt_payload['sub'] = self._tech_acc_id
        # audience
        jwt_payload['aud'] = '{}/c/{}'.format(ReportSuite.IMS_HOST, self._client_id)
        jwt_payload['{}/s/{}'.format(ReportSuite.IMS_HOST, self._scope)] = True
        # identifier (optional)
        #payload['jti'] = ''

        # read priveate key
        private_key = ''
        with open(self._priv_key_path,'r') as f:
            private_key = f.read()

        # create jwt token
        jwt_token = jwt.encode(jwt_payload, private_key, algorithm='RS256')
        if decode:
            return jwt_token.decode('utf-8')
        return jwt_token


    def get_users(self, me=False):
        '''
            Retrieves an object containing all or the current user..

            Parameters
            ----------
            me : bool
                Return the current user only.

            Returns
            -------
            users : pyanalytics2.segments.Users or pyanalytics2.users.AnalyticsUsers
                Object containing all users or the requested user.
            err_msg : dict
                Error message.
        '''
        url = '{}/{}/users'.format(ReportSuite.BASE_API_URL,self._glob_company_id)

        if me:
            # get only the current user
            url += f'/me'
            status_code, results = self._make_request('GET', url, None)
            if status_code!=200:
                return None, results
            user = AnalyticsUser()
            user.read_response(results)
            return user, {}
        # paylaod
        params = {}
        params['page'] = 0
        params['limit'] = 300


        headers = self._get_request_headers()
        request = RankedRequest(None, None)
        results, err_msg = request.execute('GET', url, headers, params=params, proxy=self._proxy)
        if err_msg!='OK':
            return None, {'error':err_msg}

        # return users object iwth all userssegments
        all_users = []
        for item in results:
            tmp_user = AnalyticsUser()
            tmp_user.read_response(item)
            all_users.append(tmp_user)
        users = Users(all_users[0].company_id, items=all_users)
        return users, {}


    def get_dimensions(self, dim_id=None, segmentable=False, reportable=False, classifiable=False, locale='en_US'):
        '''
            Return all or a specific dimension.
            TODO: get single dimension by id

            Parameters
            ----------
            dimId : int
                ID of the desired dimension. If None, all dimensions will be returned.
            segmentable : bool
                Only include dimensions that are valid within a segment.
            reportable : bool
                Only include dimensions that are valid within a report.
            classifiable : bool
                Only include classifiable dimensions.
            locale : str
                Locale

            Returns
            -------
            users : dict
            Dict with all dimensions. Keys represent the column names.
        '''
        if dim_id is None:
            url = '{}/{}/dimensions'.format(ReportSuite.BASE_API_URL,self._glob_company_id)
        else:
            url = '{}/{}/dimensions/{}'.format(ReportSuite.BASE_API_URL,self._glob_company_id, dim_id)

        params = {}
        params['rsid'] = self._report_suite_id
        params['segmentable'] = segmentable
        params['reportable'] = reportable
        params['classifiable'] = classifiable
        params['locale'] = locale

        status_code, resp = self._make_request('GET', url, params)
        if status_code!=200:
            return {status_code:resp}

        sorted_dims = sorted(resp, key=lambda dic: len(dic.keys()), reverse=True)
        dimensions = {}
        for key in sorted_dims[0].keys():
            dimensions[key] = []

        for dim in sorted_dims:
            for key in dimensions.keys():
                try:
                    dimensions[key].append(dim[key])
                except KeyError:
                    dimensions[key].append(np.nan)
        return dimensions


    def get_metrics(self, metric_id=None, segmentable=False, locale='en_US'):
        '''
            This returns a specific or all metrics primarily for the Analytics product.
            The platform identity API Returns a list of all possible metrics for the supported systems.

            TODO: get single metric by id

            Parameters
            ----------
            metricId : int
                ID of the desired metric. If this is None, all metrics will be returned.
            segmentable : bool
                Filter the metrics by if they are valid in a segment
            locale : str
                Locale that system named metrics should be returned in.

            Returns
            -------
            users : dict
            Dict with all metrics. Keys represent the column names.

        '''
        if metric_id is None:
            url = '{}/{}/metrics'.format(ReportSuite.BASE_API_URL,self._glob_company_id)
        else:
            url = '{}/{}/metrics/{}'.format(ReportSuite.BASE_API_URL,self._glob_company_id, metric_id)

        params = {}
        params['rsid'] = self._report_suite_id
        params['segmentable'] = segmentable
        params['locale'] = locale

        status_code, resp = self._make_request('GET', url, params)
        if status_code!=200:
            return {status_code:resp}

        sorted_mets = sorted(resp, key=lambda dic: len(dic.keys()), reverse=True)
        metrics = {}
        for key in sorted_mets[0].keys():
            metrics[key] = []

        for met in sorted_mets:
            for key in metrics.keys():
                try:
                    metrics[key].append(met[key])
                except KeyError:
                    metrics[key].append(np.nan)
        return metrics


    def _make_request(self, method, url, data, use_org_id=False):
        headers = self._get_request_headers(use_org_id)
        try:
            if method=='GET':
                if self._proxy is None:
                    r = req.get(url, params=data, headers=headers)
                else:
                    r = req.get(url, params=data, headers=headers, proxies=self._proxy)
            elif method=='POST':
                pass
        except req.exceptions.ProxyError:
            print('PROXY EROR:', url)
            return 502, {}
        return r.status_code, r.json()


    def _get_request_headers(self, use_org_id=False):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'
        headers['x-api-key'] = self._client_id
        headers['Authorization'] = 'Bearer ' + self._access_token
        if use_org_id:
            headers['x-proxy-global-company-id'] = self._org_id
        else:
            headers['x-proxy-global-company-id'] = self._glob_company_id
        return headers


    def get_segment(self, segment_id=None, include_type='all', rsids=[], segment_filter=[], locale='en_US', name='',
                     tag_names='', limit=300, page=0):
        '''
            Retrieve a single segment by ID or all segments.

            Parameters
            ----------
            include_type : str
                Include additional segments not owned by user. The “all” option takes precedence over “shared”
                Available options: shared, all, templates, deleted, internal, curatedItem
            rsids : list
                Filter list to only include segments tied to specified RSID list.
            segment_filter : list
                Filter list to only include segments in the specified list.
            locale : str
                Locale.
            name : str
                Filter list to only include segments that contains the Name.
            tag_names : str
                Filter list to only include segments that contains one of the tags
            limit : int
                Number of results per page/request.
            page : int
                Page number (base 0 - first page is “0”)

            Returns
            -------
            segments : pyanalytics2.segments.Segments or pyanalytics2.segments.AnalyticsSegmentResponseItem
                Object containing all segments or the requested item.
            err_msg : dict
                Error message.
        '''
        url = '{}/{}/segments'.format(ReportSuite.BASE_API_URL, self._glob_company_id)
        headers = self._get_request_headers()

        params = {}
        if segment_id is None:
            params['limit'] = limit
            params['page'] = page
            params['includeType'] = include_type
            if len(rsids)>0:
                params['rsids'] = ','.join(rsids)
            if len(segment_filter)>0:
                params['segmentFilter'] = ','.join(segment_filter)
            if len(name)>0:
                params['name'] = ','.join(name)
            if len(tag_names)>0:
                params['tagNames'] = ','.join(tag_names)
        else:
            url += f'/{segment_id}'
        params['locale'] = locale
        params['expansion'] = 'reportSuiteName,ownerFullName,modified,tags,compatibility,definition'

        request = RankedRequest(None, None)
        results, err_msg = request.execute('GET', url, headers, params=params, proxy=self._proxy)
        if err_msg!='OK':
            return None, {'error':err_msg}

        # handle single segment
        if segment_id is not None:
            segment = AnalyticsSegmentResponseItem()
            segment.read_response(results)
            return segment, {}

        # return segments object with all segments
        all_segments = []
        for item in results:
            tmp_segment = AnalyticsSegmentResponseItem()
            tmp_segment.read_response(item)
            all_segments.append(tmp_segment)
        segments = Segments(include_type, rsids, locale, items=all_segments)
        return segments, {}


    def get_report(self, request, params=None):
        '''
            Download a report.

            Parameters
            ----------
            request : pyanalytics2.models.ranked_request.RankedRequest
                Request object containing all necessary parameters

            Returns
            -------
            report : pyanalytics2.report.Report
                Report object.
            err_msg : dict
                Error message.
        '''
        url = '{}/{}/reports'.format(ReportSuite.BASE_API_URL, self._glob_company_id)
        headers = self._get_request_headers()
        if params is None:
            results, err_msg = request.execute('POST', url, headers, proxy=self._proxy)
        else:
            results, err_msg = request.execute('POST', url, headers, params=params, proxy=self._proxy)
        if err_msg!='OK':
            return None, {'error':err_msg}
        rows = list(it.chain.from_iterable([d['rows'] for d in results]))

        # create report dimension
        col_ids = results[0]['columns']['columnIds']
        if 'dimension' in results[0]['columns'].keys():
            dim_id = results[0]['columns']['dimension']['id']
            dim_type = results[0]['columns']['dimension']['type']
        else:
            dim_id = None
            dim_type = None
        rep_dim = ReportDimension(dim_id, dim_type)

        # add errors if any occured
        all_rce = []
        for rce in results[0]['columns'].get('columnErrors', []):
            err_col_id = rce['columnId']
            err_code = rce['errorCode']
            err_id = rce['errorId']
            err_descr = rce['errorDescription']
            all_rce.append(RankedColumnError(err_col_id,err_code, err_id, err_descr))
        meta_data = RankedColumnMetaData(rep_dim, col_ids, all_rce)

        # create Report object and add data
        report = Report(request, meta_data)
        for r in rows:
            rparams = {}
            try:
                rparams['item_id'] = r['itemId']
                rparams['value'] = r['value']
                rparams['data'] = r['data']
            except KeyError:
                continue
            rparams['row_id'] = r.get('rowId', '')
            rparams['data_expected'] = r.get('dataExpected', [])
            rparams['data_upper_bound'] = r.get('dataUpperBound' ,[])
            rparams['data_lower_bound'] = r.get('dataLowerBound', [])
            rparams['data_anomaly_detected'] = r.get('dataAnomalyDetected',[])
            rparams['percent_change'] = r.get('percentChange', [])
            rparams['latitude'] = r.get('latitude', None)
            rparams['longitude'] = r.get('longitude', None)
            report.append(Row(**rparams))
        return report, {}


    @property
    def proxy(self):
        return self._proxy
    @proxy.setter
    def proxy(self, proxy):
        self._proxy = proxy


    @property
    def report_suite_id(self):
        return self._report_suite_id
    @report_suite_id.setter
    def report_suite_id(self, rsid):
        self._report_suite_id = rsid
    @property
    def rsid(self):
        return self._report_suite_id
    @rsid.setter
    def rsid(self, rsid):
        self._report_suite_id = rsid





