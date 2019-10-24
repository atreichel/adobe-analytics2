
import sys

import pandas as pd

from pyanalytics2.report_suite import ReportSuite
from pyanalytics2.models.ranked_request import RankedRequest
from pyanalytics2.models.report_filter import ReportFilter
from pyanalytics2.models.ranked_settings import RankedSettings
from pyanalytics2.models.report_metric import ReportMetric
from pyanalytics2.models.report_metrics import ReportMetrics

from pyanalytics2 import utils


# create and init report suite
rs_params = utils.read_config('../credentials/config')
rs = ReportSuite(**rs_params)
if not rs.init():
    print('Initialization failed.')
    sys.exit()


# create request paramters and objects
filter_params = {}
filter_params['filter_id'] = 0
filter_params['filter_type'] = 'dateRange'
filter_params['date_range'] = "2019-01-01T00:00:00.000/2019-04-12T23:59:59.999"
rfilter = ReportFilter(**filter_params)

rsettings = RankedSettings(limit=10, page=0, dimension_sort='asc')
single_metrics = [ReportMetric('metrics/pageviews', column_id=0, filters=[0])]
metric_container = ReportMetrics(single_metrics, [rfilter])

request_params = {}
request_params ['report_suite_id'] = rs.rsid
request_params ['dimension'] = 'variables/daterangeday'
request_params ['global_filters'] = [rfilter]
request_params ['settings'] = rsettings
request_params ['metric_container'] = metric_container
request_params ['pagination'] = True

request = RankedRequest(**request_params)
report, err_msg = rs.get_report(request)
if len(err_msg)>0:
    print('Failed to load report.')
    sys.exit()


cols, values = report.to_tuple_list()

report_df1 = pd.DataFrame(report.to_dict_list())
report_df2 = pd.DataFrame(report.to_dict())
report_df3 = pd.DataFrame(values, columns=cols)









