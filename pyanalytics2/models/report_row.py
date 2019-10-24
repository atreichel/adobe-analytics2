import json

class ReportRows(object):
    def __init__(self, *args, **kwargs):
        self._row_id = str(kwargs.get('row_id', ''))
        self._filters = kwargs.get('filters', [])




    def __iter__(self):
        yield 'rowId', self._row_id
        yield 'filters', self._filters


    def __repr__(self):
        return json.dumps(dict(self))

    @property
    def row_id(self):
        return self._row_id
    
    
    @property
    def filters(self):
        return self._filters
    