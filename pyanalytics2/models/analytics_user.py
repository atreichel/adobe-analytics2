import json
    
class AnalyticsUser(object):
    def __init__(self, *args, **kwargs):
        self._company_id = kwargs.get('company_id', 0)
        self._login_id = kwargs.get('login_id', 0)
        self._login = kwargs.get('login', '')
        self._change_password = kwargs.get('change_password', False)
        self._create_date = kwargs.get('create_date', '')
        self._disabled = kwargs.get('disabled', False)
        self._email = kwargs.get('email', '')
        self._first_name = kwargs.get('first_name', '')
        self._full_name = kwargs.get('full_name', '')
        self._ims_user_id = kwargs.get('ims_user_id', '')
        self._last_name = kwargs.get('last_name', '')
        self._last_login = kwargs.get('last_login', '')
        self._last_access = kwargs.get('last_access', '')
        self._phone_number = kwargs.get('phone_number', '')
        self._temp_login_end = kwargs.get('temp_login_end', '')
        self._title = kwargs.get('title', '')
        
        
        
    def read_response(self, response):
        self._company_id = response.get('companyid', self._company_id)
        self._login_id = response.get('loginId', self._login_id)
        self._login = response.get('login', self._login)
        self._change_password = response.get('changePassword', self._change_password)
        self._create_date = response.get('createDate', self._create_date)
        self._disabled = response.get('disabled', self._disabled)
        self._email = response.get('email', self._email)
        self._first_name = response.get('firstName', self._first_name)
        self._full_name = response.get('fullName', self._full_name)
        self._ims_user_id = response.get('imsUserId', self._ims_user_id)
        self._last_name = response.get('lastName', self._last_name)
        self._last_login = response.get('lastLogin', self._last_login)
        self._last_access = response.get('lastAccess', self._last_access)
        self._phone_number = response.get('phoneNumber', self._phone_number)
        self._temp_login_end = response.get('tempLoginEnd', self._temp_login_end)
        self._title = response.get('title', self._title)
    
    
    
    def __iter__(self):
        yield 'companyid', self._company_id
        yield 'loginId', self._login_id
        yield 'login', self._login
        yield 'changePassword', self._change_password
        yield 'createDate', self._create_date
        yield 'disabled', self._disabled
        yield 'email', self._email
        yield 'firstName', self._first_name
        yield 'fullName', self._full_name
        yield 'imsUserId', self._ims_user_id
        yield 'lastName', self._last_name
        yield 'lastLogin', self._last_login
        yield 'lastAccess', self._last_access
        yield 'phoneNumber', self._phone_number
        yield 'tempLoginEnd', self._temp_login_end
        yield 'title', self._title
    
    
    def __repr__(self):
        return json.dumps(dict(self))
    
       
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    
    
    @property
    def temp_login_end(self):
        return self._temp_login_end
    @temp_login_end.setter
    def temp_login_end(self, temp_login_end):
        self._temp_login_end = temp_login_end
    
    
    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number
    
    
    @property
    def last_access(self):
        return self._last_access
    @last_access.setter
    def last_access(self, last_access):
        self._last_access = last_access
    
    
    @property
    def company_id(self):
        return self._company_id
    @company_id.setter
    def company_id(self, company_id):
        self._company_id = company_id
    
    
    @property
    def login_id(self):
        return self._login_id
    @login_id.setter
    def login_id(self, login_id):
        self._login_id = login_id
        
    
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, login):
        self._login = login
        
    
    @property
    def change_password(self):
        return self._change_password
    @change_password.setter
    def change_password(self, change_password):
        self._change_password = change_password
        
    
    @property
    def create_date(self):
        return self._create_date
    @create_date.setter
    def create_date(self, create_date):
        self._create_date = create_date
        
    
    @property
    def disabled(self):
        return self._disabled
    @disabled.setter
    def disabled(self, disabled):
        self._disabled = disabled
        
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
        
    
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
        
    
    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name
        
    
    @property
    def ims_user_id(self):
        return self._ims_user_id
    @ims_user_id.setter
    def ims_user_id(self, ims_user_id):
        self._ims_user_id = ims_user_id
        
    
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
        
    
    @property
    def last_login(self):
        return self._last_login
    @last_login.setter
    def last_login(self, last_login):
        self._last_login = last_login
        
    
    