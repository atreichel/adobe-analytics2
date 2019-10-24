
from pyanalytics2.models.row import Row

class Report(object):
    COL_MAPPING = {}
    COL_MAPPING['itemId'] = 'item_id'
    COL_MAPPING['rowId'] = 'row_id'
    COL_MAPPING['dataExpected'] = 'data_expected'
    COL_MAPPING['dataUpperBound'] = 'data_upper_bound'
    COL_MAPPING['dataLowerBound'] = 'data_lower_bound'
    COL_MAPPING['dataAnomalyDetected'] = 'data_anomaly_detected'
    COL_MAPPING['percentChange'] = 'percent_change'
    COL_MAPPING['value'] = 'value'
    COL_MAPPING['data'] = 'data'
    COL_MAPPING['latitude'] = 'latitude'
    COL_MAPPING['longitude'] = 'longitude'


    def __init__(self, request, meta_data, rows=None, summary=None):
        self._request = request
        self._meta_data = meta_data
        self._summary = summary
        self._rows = rows
        if rows is None:
            self._rows = list()
        else:
            self._rows = rows


    def append(self, row):
        '''
            Add row to report.

            Parameters
            ----------
            row : pyanalytics2.models.row.Row
                Row object with data.

            Returns
            -------
             : bool
                 Indicate wether operation was successful or not.

        '''
        if not isinstance(row, Row):
            return False
        self._rows.append(row)
        return True


    def to_dict_list(self):
        '''
            Convert object ot list of dictionaries.
            Does not return empty columns.

            Returns
            -------
            values : list
            List of dicts.
        '''
        col_ids = self._meta_data.column_ids
        rows = [dict(e) for e in self._rows]
        values = []
        for row in rows:
            tmp_dict = {}
            for key, val in row.items():
                key = Report.COL_MAPPING[key]
                if val is None:
                    continue
                elif isinstance(val, list) and len(val)==0:
                    continue
                elif isinstance(val, list) and len(val)>0:
                    for i, cid in enumerate(col_ids):
                        tmp_dict[f'{key}_{cid}'] = val[i]
                else:
                    tmp_dict[key] = val
            tmp_dict['dimension_id'] = self._meta_data.dimension.dimension_id
            tmp_dict['dimension_type'] = self._meta_data.dimension.dimension_type
            values.append(tmp_dict)
        return values


    def to_tuple_list(self):
        '''
            Convert object ot list of tuples.

            Returns
            -------
            columns : tuple
                Column names.
            values : list
                List of tuples.
        '''
        col_ids = self._meta_data.column_ids
        rows = [dict(e) for e in self._rows]
        values = []
        columns = []
        for row in rows:
            tmp_dict = {}
            for key, val in row.items():
                key = Report.COL_MAPPING[key]
                if val is None:
                    continue
                elif isinstance(val, list) and len(val)==0:
                    continue
                elif isinstance(val, list) and len(val)>0:
                    for i, cid in enumerate(col_ids):
                        tmp_dict[f'{key}_{cid}'] = val[i]
                else:
                    tmp_dict[key] = val
            tmp_dict['dimension_id'] = self._meta_data.dimension.dimension_id
            tmp_dict['dimension_type'] = self._meta_data.dimension.dimension_type
            values.append(tuple(tmp_dict.values()))
            columns = tuple(tmp_dict.keys())
        return columns, values



    def to_dict(self):
        '''
            Convert object to dictionary

            Returns
            -------
            result : dict
                dict conversion.
        '''
        result = {}
        result['dimension_id'] = []
        result['dimension_type'] = []
        result['item_id'] = []
        result['value'] = []
        result['row_id'] = []
        result['latitude'] = []
        result['longitude'] = []
        for cid in self._meta_data.column_ids:
            result[cid] = []
            result['data_expected_'+cid] = []
            result['data_upper_bound_'+cid] = []
            result['data_lower_bound_'+cid] = []
            result['data_anomaly_detected_'+cid] = []
            result['percent_change_'+cid] = []

        for r in self._rows:
            result['dimension_id'].append(self._meta_data.dimension.dimension_id)
            result['dimension_type'].append(self._meta_data.dimension.dimension_type)
            result['item_id'].append(r.item_id)
            result['value'].append(r.value)
            result['row_id'].append(r.row_id)
            result['latitude'].append(r.latitude)
            result['longitude'].append(r.longitude)
            for i, cid in enumerate(self._meta_data.column_ids):
                result[cid].append(r.data[i])
                if len(r.percent_change)>0:
                    result['percent_change_'+cid].append(r.percent_change[i])
                else:
                    result['percent_change_'+cid].append(None)
                if len(r.data_expected)>0:
                    result['data_expected_'+cid].append(r.data_expected[i])
                else:
                    result['data_expected_'+cid].append(None)
                if len(r.data_upper_bound)>0:
                    result['data_upper_bound_'+cid].append(r.data_upper_bound[i])
                else:
                    result['data_upper_bound_'+cid].append(None)
                if len(r.data_lower_bound)>0:
                    result['data_lower_bound_'+cid].append(r.data_lower_bound[i])
                else:
                    result['data_lower_bound_'+cid].append(None)
                if len(r.data_anomaly_detected)>0:
                    result['data_anomaly_detected_'+cid].append(r.data_anomaly_detected[i])
                else:
                    result['data_anomaly_detected_'+cid].append(None)
        return result


    def __repr__(self):
        return 'No. rows:\t{}\nMeta data:\t{}'.format(len(self._rows),self._meta_data)


    @property
    def request(self):
        return self._request

    @property
    def meta_data(self):
        return self._meta_data

    @property
    def rows(self):
        return self._rows

    @property
    def size(self):
        return len(self._rows)



