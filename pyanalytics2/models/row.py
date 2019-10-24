
import json 


class Row(object):
    def __init__(self, item_id, value, data, *args, **kwargs):
        self._item_id = item_id
        self._value = value
        self._data = data
        self._row_id = kwargs.get('row_id', None)
        self._data_expected = kwargs.get('data_expected', None)
        self._data_upper_bound = kwargs.get('data_upper_bound', None)
        self._data_lower_bound = kwargs.get('data_lower_bound', None)
        self._data_anomaly_detected = kwargs.get('data_anomaly_detected', None)
        self._percent_change = kwargs.get('percent_change', None)
        self._latitude = kwargs.get('latitude', None)
        self._longitude = kwargs.get('longitude', None)



    def __iter__(self):
        yield 'itemId', self._item_id
        yield 'value', self._value
        yield 'data', self._data
        yield 'rowId', self._row_id
        yield 'dataExpected', self._data_expected
        yield 'dataUpperBound', self._data_upper_bound
        yield 'dataLowerBound', self._data_lower_bound
        yield 'dataAnomalyDetected', self._data_anomaly_detected
        yield 'percentChange', self._percent_change
        yield 'latitude', self._latitude
        yield 'longitude', self._longitude



    def __repr__(self):
        return json.dumps(dict(self))

    @property
    def item_id(self):
        return self._item_id

    @property
    def value(self):
        return self._value

    @property
    def data(self):
        return self._data

    @property
    def row_id(self):
        return self._row_id

    @property
    def data_expected(self):
        return self._data_expected

    @property
    def data_upper_bound(self):
        return self._data_upper_bound

    @property
    def data_lower_bound(self):
        return self._data_lower_bound

    @property
    def data_anomaly_detected(self):
        return self._data_anomaly_detected

    @property
    def percent_change(self):
        return self._percent_change

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

