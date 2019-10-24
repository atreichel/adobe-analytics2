import json
    
class Owner(object):
    def __init__(self, owner_id=0, name='Unknown User', login=''):
        self._owner_id = owner_id
        self._name = name
        self._login = login

    
    
    def __iter__(self):
        yield 'id', self._owner_id
        yield 'name', self._name
        yield 'login', self._login
      
        
    def __repr__(self):
        return json.dumps(dict(self))
    
    
    @property
    def owner_id(self):
        return self._owner_id
    @owner_id.setter
    def owner_id(self, owner_id):
        self._owner_id = owner_id
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, login):
        self._login = login
        

        