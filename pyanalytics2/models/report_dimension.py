
import json 


class 	ReportDimension(object):
    '''
        Report dimension.
        
        Parameters
        ----------
        dim_id : str
            ID of the dimension.
        dim_type : str
            Type of ythe dimensions.
            [ STRING, INT, DECIMAL, CURRENCY, PERCENT, TIME, ENUM, ORDERED_ENUM ]
    '''
    def __init__(self, dim_id, dim_type):
        self._dim_id = dim_id
        self._dim_type = dim_type


    def __iter__(self):
        yield 'id', self._dim_id
        yield 'type', self._dim_type


    def __repr__(self):
        return json.dumps(dict(self))



    @property
    def dimension_id(self):
        return self._dim_id

    @property
    def dimension_type(self):
        return self._dim_type

