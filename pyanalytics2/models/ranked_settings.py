import json

class RankedSettings(object):
    def __init__(self, *args, **kwargs):
        self._limit = kwargs.get('limit', 500)
        self._page = kwargs.get('page', 0)
        self._dimension_sort = kwargs.get('dimension_sort', 'asc')
        self._count_repeat_instances = kwargs.get('count_repeat_instances', False)
        self._reflect_requests = kwargs.get('reflect_request', False)
        self._include_anomaly_detection = kwargs.get('include_anomaly_detection', False)
        self._include_percent_change = kwargs.get('include_percent_change', False)
        self._include_lat_long = kwargs.get('include_lat_long', False)
        
        
    def __iter__(self):
        yield 'limit', self._limit
        yield 'page', self._page
        yield 'countRepeatInstances', self._count_repeat_instances
        yield 'reflectRequest', self._reflect_requests
        yield 'includeAnomalyDetection', self._include_anomaly_detection
        yield 'includePercentChange', self._include_percent_change
        yield 'includeLatLong', self._include_lat_long
        if len(self._dimension_sort)>0:
            yield 'dimensionSort', self._dimension_sort

    
    def __repr__(self):
        return json.dumps(dict(self))

    
    @property
    def limit(self):
        return self._limit
        
    @property
    def page(self):
        return self._page
        
    @property
    def dimension_sort(self):
        return self._dimension_sort
        
    @property
    def count_repeat_instances(self):
        return self._count_repeat_instances
        
    @property
    def reflect_request(self):
        return self._reflect_request
        
    @property
    def include_anomaly_detection(self):
        return self._include_anomaly_detection
        
    @property
    def include_percent_change(self):
        return self._include_percent_change
        
    @property
    def include_lat_long(self):
        return self._include_lat_long