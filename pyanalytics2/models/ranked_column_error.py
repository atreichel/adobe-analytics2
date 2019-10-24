
import json 


class 	RankedColumnError(object):
    '''
        Ranked column error.
        
        Parameters
        ----------
        column_id : str
            ...
        error_code : str
            [ unauthorized_metric, unauthorized_dimension, unauthorized_dimension_global, anomaly_detection_failure_unexpected_item_count, anomaly_detection_failure_tsa_service, not_enabled_metric, not_enabled_dimension, not_enabled_dimension_global]
        error_id : str
            ...
        error_descr : str
            ...
    '''
    def __init__(self, column_id, error_code, error_id, error_descr):
        self._column_id = column_id
        self._error_code = error_code
        self._error_id = error_id
        self._error_descr = error_descr


    def __iter__(self):
        yield 'columnId', self._column_id
        yield 'errorCode', self._error_code
        yield 'errorId', self._error_id
        yield 'errorDescription', self._error_descr


    def __repr__(self):
        return json.dumps(dict(self))


    @property
    def column_id(self):
        return self._column_id

    @property
    def error_code(self):
        return self._error_code

    @property
    def error_id(self):
        return self._error_id

    @property
    def error_descr(self):
        return self._error_descr