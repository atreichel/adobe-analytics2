import json


class ReportSearch(object):
    '''
        Filter results in a request.
        
        Parameters
        ----------
        item_ids : list
            A list of itemIds to include in the report.
        exclude_item_ids : list
            A list of itemIds to exclude in the report.
        clause : str
            A search clause to use when filtering dimensions.
            
            Available parameters:
                AND
                OR
                NOT
                MATCH
                BEGINNS-WITHH
                ENDS-WITH
                \*
            E.g. (NOT CONTAINS 'home page' OR NOT CONTAINS 'about us') AND (CONTAINS 'contact us')
                
        include_search_total : bool
            Includes a special element called 'searchTotals' in the response that contains the 
            total of the filtered items.
        empty : bool
            -
    '''
    def __init__(self, *args, **kwargs):
        self._clause = kwargs.get('clause', '')
        self._exclude_item_ids = kwargs.get('exclude_item_ids', [])
        self._item_ids = kwargs.get('item_ids', [])
        self._empty = kwargs.get('empty', None)
        self._include_search_total = kwargs.get('include_search_total', None)     



    def __iter__(self):
        if len(self._clause)>0:
            yield 'clause', self._clause
        if len(self._exclude_item_ids)>0:
            yield 'excludeItemIds', self._exclude_item_ids
        if len(self._item_ids)>0:
            yield 'itemIds', self._item_ids
        if self._include_search_total is not None:
            yield 'includeSearchTotal', self._include_search_total
        if self._empty is not None:            
            yield 'empty', self._empty
        
        

    def __repr__(self):
        return json.dumps(dict(self))
    

    @property
    def clause(self):
        return self._clause
    
    
    @property
    def exclude_item_ids(self):
        return self._exclude_item_ids
    
    
    @property
    def item_ids(self):
        return self._item_ids
    
    
    @property
    def empty(self):
        return self._empty
    
    
    @property
    def include_search_total(self):
        return self._include_search_total

