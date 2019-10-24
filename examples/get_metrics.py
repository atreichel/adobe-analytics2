
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

# get metrics
metrics = pd.DataFrame(rs.get_metrics(metric_id=None))
#metrics.to_csv('metrics.csv', index=None)