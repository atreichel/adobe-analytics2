
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

# get all segments
segments, err_msg = rs.get_segment()
print(segments)
if len(err_msg)>0:
    print('Failed to load segments.')
    sys.exit()

segments_df = pd.DataFrame(segments.to_dict())
#segments_df.to_csv('segments.csv', index=None)


# get a segment by ID
segment_id = segments.items[0].item_id
segment, err_msg = rs.get_segment(segment_id=segment_id)

