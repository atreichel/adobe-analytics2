import json

class ReportMetrics(object):
    def __init__(self, metrics, filters=[]):
        self._metric_filters = filters
        self._metrics = metrics


    def __iter__(self):
        yield 'metrics', [dict(f) for f in self._metrics]
        yield 'metricFilters', [dict(f) for f in self._metric_filters]


    def __repr__(self):
        return json.dumps(dict(self))
    

    @property
    def metric_filters(self):
        return self._metric_filters
    
    @property
    def metrics(self):
        return self._metrics

