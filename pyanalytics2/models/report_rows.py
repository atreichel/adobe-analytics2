import json


class ReportRows(object):
    def __init__(self, *args, **kwargs):
        self._row_filters = kwargs.get('row_filters', [])
        self._rows = kwargs.get('rows', [])

    
  


    def __iter__(self):
        yield 'rows', [dict(r) for r in self._rows]
        yield 'rowFilters', [dict(f) for f in self._row_filters]


    def __repr__(self):
        return json.dumps(dict(self))      


    @property
    def row_filters(self):
        return self._row_filters
    
    
    @property
    def rows(self):
        return self._rows
    