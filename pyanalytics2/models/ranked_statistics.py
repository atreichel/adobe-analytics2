import json


class RankedStatistics(object):
    def __init__(self, *args, **kwargs):
        self._functions = kwargs.get('functions', [])
        self._ignore_zeroess = kwargs.get('ignore_zeroes', False)



    def __iter__(self):
        yield 'functions', self._functions
        yield 'ignoreZeroes', self._ignore_zeroess
        
        

    def __repr__(self):
        return json.dumps(dict(self))
    
        
    @property
    def functions(self):
        return self._functions
    
    
    @property
    def ignore_zeroes(self):
        return self._ignore_zeroes
    

    