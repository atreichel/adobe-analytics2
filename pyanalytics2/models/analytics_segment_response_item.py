import json

from pyanalytics2.models.owner import Owner
from pyanalytics2.models.tag import Tag
from pyanalytics2.models.tagged_component import TaggedComponent

    
class AnalyticsSegmentResponseItem(object):
    def __init__(self, *args, **kwargs):
        self._item_id = str(kwargs.get('item_id', 0))
        self._name = kwargs.get('name', '')
        self._description = kwargs.get('description', '')
        self._rsid = kwargs.get('rsid', '')
        self._report_suite_name = kwargs.get('report_suite_name', '')
        self._owner = kwargs.get('owner', Owner())
        self._definition = kwargs.get('definition', {})
        self._compatibility = kwargs.get('compatibility', {})
        self._version = kwargs.get('version', '')
        self._site_title = kwargs.get('site_title', '')
        self._tags = kwargs.get('tags', [])
        self._modified = kwargs.get('modified', '')
        self._created = kwargs.get('created', '')
        
        
        
        
    def read_response(self, response):
        self._item_id = response.get('id', self._item_id)
        self._name = response.get('name', self._name)
        self._description = response.get('description', self._description)
        self._report_suite_name = response.get('reportSuiteName', self._report_suite_name)
        self._rsid = response.get('rsid', self._rsid)
        self._definition = response.get('definition', self._definition)
        self._compatibility = response.get('compatibility', self._compatibility)
        self._version = response.get('version', self._version)
        self._site_title = response.get('siteTitle', self._site_title)
        self._modified = response.get('modified', self._modified)
        self._created = response.get('created', self._created)

        if 'owner' in response.keys():
            oid = response['owner']['id']
            name = response['owner']['name']
            login = response['owner']['login']
            self._owner = Owner(oid, name, login)
        if 'tags' in response.keys():
            for tag in response['tags']:
                # tag params
                tid = tag.get('id', '')
                name = tag.get('name', '')
                description = tag.get('description', '')
                
                # tagged comp params
                components = []
                for tc in tag['components']:
                    comp_type = tag['components']['componentType']
                    comp_id = tag['components']['componentId']
                    tags = tag['components']['tags']
                    components.append(TaggedComponent(comp_id, comp_type, tags))
                self._tags.append(Tag(tid, name, description, components))

    
    
    def __iter__(self):
        yield 'id', self._item_id
        yield 'name', self._name
        yield 'description', self._description
        yield 'rsid', self._rsid
        yield 'reportSuiteName', self._report_suite_name
        yield 'owner', dict(self._owner)
        yield 'definition', self._definition
        yield 'compatibility', self._compatibility
        yield 'version', self._version
        yield 'siteTitle', self._site_title
        yield 'tags', [dict(t) for t in self._tags]
        yield 'modified', self._modified
        yield 'created', self._created

  
        
    def __repr__(self):
        return json.dumps(dict(self))
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    
    @property
    def report_suite_id(self):
        return self._rsid
    @report_suite_id.setter
    def report_suite_id(self, rsid):
        self._rsid = rsid
        
    
    @property
    def report_suite_name(self):
        return self._report_suite_name
    @report_suite_name.setter
    def report_suite_name(self, report_suite_name):
        self._report_suite_name = report_suite_name
        
    
    @property
    def item_id(self):
        return self._item_id
    @item_id.setter
    def item_id(self, item_id):
        self._item_id = item_id
        
    
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        self._owner = owner
        
    
    @property
    def definition(self):
        return self._definition
    @definition.setter
    def definition(self, definition):
        self._definition = definition
        
    
    @property
    def compatibility(self):
        return self._compatibility
    @compatibility.setter
    def compatibility(self, compatibility):
        self._compatibility = compatibility
        
    
    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version
        
    
    @property
    def site_title(self):
        return self._site_title
    @site_title.setter
    def site_title(self, site_title):
        self._site_title = site_title
        
    
    @property
    def created(self):
        return self._created
    @created.setter
    def created(self, created):
        self._created = created
        
    
    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags
        
    
    @property
    def modified(self):
        return self._modified
    @modified.setter
    def modified(self, modified):
        self._modified = modified
        
    
    