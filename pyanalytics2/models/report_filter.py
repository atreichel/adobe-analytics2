import json
    
class ReportFilter(object):
    def __init__(self, *args, **kwargs):
        self._filter_id = str(kwargs.get('filter_id', ''))
        self._filter_type = kwargs.get('filter_type', '') #[ dateRange, BREAKDOWN, SEGMENT, EXCLUDE_ITEM_IDS]
        self._dimension = kwargs.get('dimension', '')
        self._item_id = str(kwargs.get('item_id', ''))
        self._item_ids = [str(i) for i in kwargs.get('item_ids', [])]
        self._segment_id = str(kwargs.get('segment_id', ''))
        self._segment_definition = kwargs.get('segment_definition', {})
        self._date_range = kwargs.get('date_range', '')
        self._exclude_item_ids = [str(i) for i in kwargs.get('exclude_item_ids', [])]
        
    
    
    def __iter__(self):
        if len(self._filter_type)>0:
            yield 'type', self._filter_type
        if len(self._filter_id)>0:
            yield 'id', self._filter_id
        if len(self._dimension)>0:
            yield 'dimension', self._dimension
        if len(self._item_id)>0:
            yield 'itemId', self._item_id
        if len(self._item_ids)>0:
            yield 'itemIds', self._item_ids
        if len(self._segment_id)>0:
            yield 'segmentId', self._segment_id
        if len(self._date_range)>0:
            yield 'dateRange', self._date_range
        if len(self._exclude_item_ids)>0:
            yield 'excludeItemIds', self._exclude_item_ids
        if len(self._segment_definition)>0:
            yield 'segmentDefinition', self._segment_definition

      
        
    def __repr__(self):
        return json.dumps(dict(self))
    
    
    @property
    def filter_id(self):
        return self._filter_id
    @filter_id.setter
    def filter_id(self, fid):
        self._filter_id = str(fid)
    
    @property
    def filter_type(self):
        return self._filter_type
    
    @property
    def dimension(self):
        return self._dimension
    
    @property
    def item_id(self):
        return self._item_id
    
    @property
    def item_ids(self):
        return self._item_ids
    
    @property
    def segment_id(self):
        return self._segment_id
    
    @property
    def segment_definition(self):
        return self._segment_definition
    
    @property
    def date_range(self):
        return self._date_range
    
    @property
    def exclude_item_ids(self):
        return self._exclude_item_ids