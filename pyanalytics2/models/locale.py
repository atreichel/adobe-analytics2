import json


class Locale(object):
    def __init__(self, *args, **kwargs):
        self._language = kwargs.get('language', 'en_US') #Supported values are en_US, fr_FR, jp_JP, ja_JP, de_DE, es_ES, ko_KR, pt_BR, zh_CN, and zh_TW
        self._script = kwargs.get('script', '')
        self._country = kwargs.get('country', '')
        self._variant = kwargs.get('variant', '')
        self._extension_keys = kwargs.get('extension_keys', [])
        self._unicode_locale_attributes = kwargs.get('unicode_locale_attributes', [])
        self._unicode_locale_keys = kwargs.get('unicode_locale_keys', [])
        self._iso3_language = kwargs.get('iso3_language', '')
        self._iso3_country = kwargs.get('iso3_country', '')
        self._display_language = kwargs.get('display_language', '')
        self._display_script = kwargs.get('display_script', '')
        self._display_country = kwargs.get('display_country', '')
        self._display_variant = kwargs.get('display_variant', '')
        self._display_name = kwargs.get('display_name', '')



    def __iter__(self):
        yield 'language', self._language
        yield 'script', self._script
        yield 'country', self._country
        yield 'variant', self._variant
        yield 'extensionKeys', self._extension_keys
        yield 'unicodeLocaleAttributes', self._unicode_locale_attributes
        yield 'unicodeLocaleKeys', self._unicode_locale_keys
        yield 'iso3Language', self._iso3_language
        yield 'iso3Country', self._iso3_country
        yield 'displayLanguage', self._display_language
        yield 'displayScript', self._display_script
        yield 'displayCountry', self._display_country
        yield 'displayVariant', self._display_variant
        yield 'displayName', self._display_name
        
       

    def __repr__(self):
        return json.dumps(dict(self))
    
    
        
    @property
    def language(self):
        return self._language
        
    @property
    def script(self):
        return self._script
        
    @property
    def country(self):
        return self._country
        
    @property
    def variant(self):
        return self._variant
        
    @property
    def extension_keys(self):
        return self._extension_keys
        
    @property
    def unicode_locale_attributes(self):
        return self._unicode_locale_attributes
        
    @property
    def unicode_locale_keys(self):
        return self._unicode_locale_keys
        
    @property
    def iso3_language(self):
        return self._iso3_language
        
    @property
    def _iso3_country(self):
        return self.iso3_country
        
    @property
    def _display_language(self):
        return self.display_language
        
    @property
    def display_script(self):
        return self._display_script
        
    @property
    def display_country(self):
        return self._display_country
        
    @property
    def display_variant(self):
        return self._display_variant
        
    @property
    def display_name(self):
        return self._display_name