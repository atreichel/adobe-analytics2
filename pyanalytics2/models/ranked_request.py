
import json
import time

import requests as req

class RankedRequest(object):
    def __init__(self,report_suite_id, dimension=None, *args, **kwargs):
        self._rsid = report_suite_id
        self._dimension = dimension
        self._locale = kwargs.get('locale', None)
        self._global_filters = kwargs.get('global_filters',[])
        self._search = kwargs.get('search', None)
        self._settings = kwargs.get('settings', None)
        self._statistics = kwargs.get('statistics', None)
        self._metric_container = kwargs.get('metric_container', None)
        self._row_container = kwargs.get('row_container', None)
        self._anchor_date = kwargs.get('anchor_date', '')   
        
        self._pagination = kwargs.get('pagination', True) 
        self._headers = kwargs.get('headers', {}) 
        self._timeout = kwargs.get('timeout', 0.5) 
    
    
    
#    def from_dict(self, dict_obj):
#        '''
#            TODO .
#        '''
#        try:
#            self._rsid = dict_obj['rsid']
#            self._dimension = dict_obj['dimension']
#        except Exception as e:
#            print('DEBUG', e)
#            return False
#        self._locale = dict_obj.get('locale', None)
#        self._global_filters = dict_obj.get('global_filters',[])
#        self._search = dict_obj.get('search', None)
#        self._settings = dict_obj.get('settings', None)
#        self._statistics = dict_obj.get('statistics', None)
#        self._metric_container = dict_obj.get('metric_container', None)
#        self._row_container = dict_obj.get('row_container', None)
#        self._anchor_date = dict_obj.get('anchor_date', '')   

     
        
    
    def execute(self, method, url, headers, params=None, proxy=None):
        '''
            Run the request.
            
            Parameters
            ----------
            method : str
                Type of request. Currently only GET and POST supported.
            url : str
                URL of the request.
            headers : dict
                Request headers.
            params : dict
                Overwrite current parameters for the request.
            proxy : dict
                Proxy URLs and ports.
            
            Returns
            -------
            results : list
                List containing the request data.
            err_msg : dict
                Error message.
        '''
        results = []
        if params is None:
            params = dict(self)
        results, err_msg =  self._next(results, url, method, headers, params, proxy=proxy)
        return results, err_msg 
    
    
    
    def _next(self, results, url, method, headers, params, proxy=None):
        '''
            Iterate through all pages of the requested object.
        '''
        try:
            if method.upper()=='GET':
                if proxy is None:
                    r = req.get(url, params=params, headers=headers)
                else:
                    r = req.get(url, params=params, headers=headers, proxies=proxy)
            elif method.upper()=='POST':
                if proxy is None:
                    r = req.post(url, data=json.dumps(params), headers=headers)
                else:
                    r = req.post(url, data=json.dumps(params), headers=headers, proxies=proxy)
            else:
                return None, method+' not implemented.'
            time.sleep(self._timeout)
        except req.exceptions.ProxyError:
            return None, 'ProxyError: '+url
            
        if r.status_code!=200:
            # error
            return None, r.text
        
        # convert respone to dict
        resp = r.json()
        
        # users, metrics, etc. endpoints
        if isinstance(resp, list):
            return resp, 'OK'
        
        # check basic response structure
        if 'content' in resp.keys():
            results += resp['content']
        elif 'id' in resp.keys():
            return resp, 'OK'
        elif 'rows' in resp.keys() and 'columns' in resp.keys():
            results.append({
                    'rows':resp['rows'],
                    'columns':resp['columns'],
                    'summary':resp['summaryData'],
                    })
        elif 'summaryData' in resp.keys() and resp['summaryData']['totals'][0]!=0:
        # segment breakdown
            results.append({
                    'rows':[{
                            'itemId':'-1',
                            'value':'-1',
                            'data':resp['summaryData']['totals'],
                    }],
                    'columns':resp['columns'],
                    'summary':resp['summaryData'],
                    })
        else:
            return resp, 'Unknown response type (might need to be implemented).'

        # number of rows already downloaded        
#        nbr_elem_per_call = [len(e['rows']) for e in results]
#        tot_nbr_elem = sum(nbr_elem_per_call)
#        tot_nbr_elem = resp['numberOfElements']*len(results)
#        
#        # stop if limit reached
#        if tot_nbr_elem>=params['settings']['limit']:
#            return results, 'OK'
        
        # no pagination
        if not self._pagination:
            return results, 'OK'
        
        # exit or go to next page
        if resp['totalElements']==0 or resp['lastPage']==True:
            return results, 'OK'
        
        # increment to next page
        if 'page' in params.keys():
            params['page'] += 1
        elif 'settings' in params.keys():
            params['settings']['page'] += 1
        else:
            return None, 'No page parameter found.'
        return self._next(results, url, method, headers, params, proxy=proxy)
        
        
        
        
    def __iter__(self):
        '''
            Convert object to dictionary.
        '''
        yield 'rsid', self._rsid
        
        if self._dimension is not None:
            yield 'dimension', self._dimension
        
        if len(self._global_filters)>0:
            yield 'globalFilters', [dict(f) for f in self._global_filters]
        
        if self._metric_container is not None:
            yield 'metricContainer', dict(self._metric_container)
        
        if self._settings is not None:
            yield 'settings', dict(self._settings)
        
        if self._locale is not None:
            yield 'locale', dict(self._locale)
        
        if self._statistics is not None:
            yield 'statistics', dict(self._statistics)
        
        if self._row_container is not None:
            yield 'rowContainer', dict(self._row_container)
        
        if len(self._anchor_date)>0:
            yield 'anchorDate', self._anchor_date
        
        if self._search is not None:
            yield 'search', dict(self._search)
        

    def __repr__(self):
        '''
            Convert object to json string.
        '''
        return json.dumps(dict(self))
    

    @property
    def report_suite_id(self):
        return self._rsid
    @report_suite_id.setter
    def report_suite_id(self, rsid):
        self._rsid = rsid
        
        
    @property
    def pagination(self):
        return self._pagination
    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination
        
        
    @property
    def timeout(self):
        return self._timeout
    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout
    
    
    @property
    def dimension(self):
        return self._dimension
    
    
    @property
    def locale(self):
        return self._locale
    
    
    @property
    def global_filters(self):
        return self._global_filters
    
    
    @property
    def search(self):
        return self._search
    
    
    @property
    def settings(self):
        return self._settings
    
    
    @property
    def statistics(self):
        return self._statistics
    
    
    @property
    def metric_container(self):
        return self._metric_container
    
    
    @property
    def row_container(self):
        return self._row_container
    
    
    @property
    def anchor_date(self):
        return self._anchor_date




