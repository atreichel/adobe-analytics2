
from pyanalytics2.models.analytics_segment_response_item import AnalyticsSegmentResponseItem


class Segments(object):
    def __init__(self, include_type, rsids, locale, items=[]):
        self._items = items
        self._include_type = include_type
        self._rsids = rsids
        self._locale = locale


    def append(self, item):
        if not isinstance(item, AnalyticsSegmentResponseItem):
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


#    def to_frame(self):
#        '''
#            Convert object to pandas.DataFrame
#            
#            TODO 
#				- probably make prettier
#				- could also be extended to search/filter items
#            
#            Returns
#            -------
#            df : pandas.DataFrame
#                DataFrame version.
#        '''
#        series = [pd.Series(dict(s)) for s in self._items]
#        df = pd.concat(series,axis=1).T
#        return df
#    
#    
#    def to_csv(self, name='segments.csv', sep=';'):
#        self.to_frame().to_csv(name, sep=sep, index=None)
        
        
    def __repr__(self):
        return 'No. items:\t{}\nIncludes types:\t{}\nRSIDs:\t{}\nLocale:\t{}'.format(
                len(self._items),self._include_type,self._rsids,self._locale)
        
        
    @property
    def items(self):
        return self._items
        
    @property
    def include_type(self):
        return self._include_type
        
    @property
    def report_suites_ids(self):
        return self._rsids
        
    @property
    def locale(self):
        return self._locale
        
