import json
    
class TaggedComponent(object):
    def __init__(self, component_id=0, component_type='', tags=[]):
        self._component_id = str(component_id)
        self._component_type = component_type
        self._tags = tags

    
    
    def __iter__(self):
        yield 'componentId', self._component_id
        yield 'componentType', self._component_type
        yield 'tags', self._tags
      
        
    def __repr__(self):
        return json.dumps(dict(self))
    
    
    @property
    def component_id(self):
        return self._component_id
    @component_id.setter
    def component_id(self, component_id):
        self._component_id = str(component_id)
    
    
    @property
    def component_type(self):
        return self._component_type
    @component_type.setter
    def component_type(self, component_type):
        self._component_type = component_type
        
    
    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags
        

        