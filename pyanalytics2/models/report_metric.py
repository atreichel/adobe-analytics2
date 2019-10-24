import json

from pyanalytics2.models.report_filter import ReportFilter

class ReportMetric(object):
    def __init__(self, metric_id, *args, **kwargs):
        self._metric_id = str(metric_id)
        self._column_id = str(kwargs.get('column_id', ''))
        
        self._filters = kwargs.get('filters', [])
        if len(self._filters)>0:
            if all(isinstance(o, ReportFilter) for o in self._filters):
                self._filters = [o.filter_id for o in self._filters]
            else:
                self._filters = [str(i) for i in self._filters]
            
        self._sort = kwargs.get('sort', '')
        self._metric_definition = kwargs.get('metric_definition', {})
        self._predictive = kwargs.get('predictive', None)
        
        
    def __iter__(self):
        yield 'id', self._metric_id
        if len(self._column_id)>0:
            yield 'columnId', self._column_id
        if len(self._filters)>0:
            yield 'filters', self._filters
        if len(self._sort)>0:
            yield 'sort', self._sort
        if len(self._metric_definition)>0:
            yield 'metricDefinition', self._metric_definition
        if self._predictive is not None:
            yield 'predictive', self._predictive

    
    def __repr__(self):
        return json.dumps(dict(self))
    
        
    @property
    def metric_id(self):
        return self._metric_id
    @metric_id.setter
    def metric_id(self, mid):
        self._metric_id = str(mid)
    
    @property
    def column_id(self):
        return self._column_id
    
    @property
    def filters(self):
        return self._filters
    @filters.setter
    def filters(self, filters):
        self._filters = [str(i) for i in filters]
    
    @property
    def sort(self):
        return self._sort
    
    @property
    def metric_definition(self):
        return self._metric_definition
    
    @property
    def predictive(self):
        return self._predictive
