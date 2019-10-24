

class ReportMetricPredictiveSettings(object):
    def __init__(self, *args, **kwargs):
        self._anomaly_confidence = kwargs.get('anomaly_confidence', 0.0)
        
        
    @property
    def anomaly_confidence(self):
        return self._anomaly_confidence