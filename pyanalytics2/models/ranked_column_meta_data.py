
import json 


class 	RankedColumnMetaData(object):
    '''
        Meta data for each column.
        
        Parameters
        ----------
        dimension : pyanalytics2.models.report_dimension
            ID and type of the requested dimension.
        column_ids : list
            Column IDs.
        column_errors : list
            Column errors.
        
    '''
    def __init__(self, dimension, column_ids, column_errors):
        self._dimension = dimension
        self._column_ids = column_ids
        self._column_errors = column_errors




    def __iter__(self):
        yield 'dimension', dict(self._dimension)
        yield 'columnIds', self._column_ids
        yield 'columnErrors', [dict(e) for e in self._column_errors]



    def __repr__(self):
        return json.dumps(dict(self))



    @property
    def dimension(self):
        return self._dimension

    @property
    def column_ids(self):
        return self._column_ids

    @property
    def column_errors(self):
        return self._column_errors

