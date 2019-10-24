
import sys

import pandas as pd

from pyanalytics2.report_suite import ReportSuite
from pyanalytics2 import utils

# create and init report suite
rs_params = utils.read_config('../credentials/config')
rs = ReportSuite(**rs_params)
if not rs.init():
    print('Initialization failed.')
    sys.exit()

# get current user
user, err_msg = rs.get_users(me=True)

# get users
users, err_msg = rs.get_users()

users_df = pd.DataFrame(users.to_dict())
#users_df.to_csv('users.csv', index=None)


cols, tup = users.to_tuple()
users_df2 = pd.DataFrame(tup, columns=cols)
