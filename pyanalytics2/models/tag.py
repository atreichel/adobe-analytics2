import json
    
class Tag(object):
    def __init__(self, tag_id=0, name='', description='', components=[]):
        self._tag_id = str(tag_id)
        self._name = name
        self._description = description
        self._components = components

    
    
    def __iter__(self):
        yield 'id', self._tag_id
        yield 'name', self._name
        yield 'description', self._description
        yield 'components', [dict(c) for c in self._components]
      
        
    def __repr__(self):
        return json.dumps(dict(self))
    
    
    @property
    def tag_id(self):
        return self._tag_id
    @tag_id.setter
    def tag_id(self, tag_id):
        self._tag_id = str(tag_id)
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description
        
    
    @property
    def components(self):
        return self._components
    @components.setter
    def item_id(self, components):
        self._components = components

        