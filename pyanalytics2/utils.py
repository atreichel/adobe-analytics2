
import os
import configparser as cp
import json


def read_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data


def read_config(path):
    '''
        Read config from file/

        Parameters
        ----------
        path : str
            Path to config file.

        Returns
        -------
        params : dict
            Configuration parameters.
    '''
    config = cp.ConfigParser()
    config.read(path)

    params = {}
    params['client_id'] = config['ACCOUNT']['ClientID']
    params['tech_acc_id'] = config['ACCOUNT']['TechnicalAccountID']
    params['tech_acc_email'] = config['ACCOUNT']['TechnicalAccountEmail']
    params['org_id'] = config['ACCOUNT']['OrganizationID']
    params['secret'] = config['ACCOUNT']['ClientSecret']
    params['private_key_path'] = config['PATHS']['PrivateKey']
    params['log_file_path'] = config['PATHS']['LogFile']
    # optional parameters
    if 'REPORTSUITE' in config and 'ReportSuiteID' in config['REPORTSUITE']:
        params['report_suite_id'] = config['REPORTSUITE']['ReportSuiteID']
    if 'PROXY' in config and 'URL' in config['PROXY'] and 'Port' in config['PROXY']:
        params['proxy'] = {'https':'{}:{}'.format(config['PROXY']['URL'],config['PROXY']['Port'])}
    else:
        params['proxy'] = None

    try:
        if len(params['log_file_path'])>0 and not os.path.isdir(params['log_file_path']):
            os.makedirs(params['log_file_path'])
    except Exception as e:
        print(e)
    return params

