
from pyanalytics2.models.analytics_user import AnalyticsUser


class Users(object):
    def __init__(self, company_id, items=[]):
        self._items = items
        self._company_id = company_id
        
        
    def append(self, item):
        if not isinstance(item, AnalyticsUser):
            return False
        self._items.append(item)
        return True
        
    
    def to_dict(self):
        '''
            Convert object ot list of dictionaries.
            
            Returns
            -------
             : list
            List of dicts.
        '''
        return [dict(i) for i in self._items]

        
    
    def to_tuple(self):
        '''
            Convert object ot list of tuples.
            
            Returns
            -------
            columns : tuple
                Column names.
            results : list
                List of tuples.
        '''
        columns = tuple(dict(self._items[0]).keys())
        results = [tuple(dict(i).values()) for i in self._items]
        return columns, results
    
            
        
    def __repr__(self):
        return 'No. users:\t{}\nCompany ID:\t{}'.format(len(self._items),self._company_id)
        
        
    @property
    def items(self):
        return self._items
        
    @property
    def company_id(self):
        return self._company_id
        

