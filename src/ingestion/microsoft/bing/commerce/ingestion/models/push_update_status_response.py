# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PushUpdateStatusResponse(Model):
    """A response that represents the status of a push data update given an update
    id.

    :param update_id: The id that uniquely identifies the push data update.
    :type update_id: str
    :param status: The wholistic update status for the push data update.
     Possible values include: 'InProgress', 'Succeeded', 'PartiallySucceeded',
     'Failed'
    :type status: str or ~microsoft.bing.commerce.ingestion.models.enum
    :param total_keys: The total number of items that are part of the upate.
    :type total_keys: int
    :param successful_keys: The total number of items that have successfully
     been updated.
    :type successful_keys: int
    :param failure_messages: An aggregation of any error messages that
     happened while ingesting any of the records.
    :type failure_messages: list[str]
    :param records: A drill down for the push update status for each record.
    :type records:
     list[~microsoft.bing.commerce.ingestion.models.ResponseRecordStatus]
    """

    _attribute_map = {
        'update_id': {'key': 'updateId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'total_keys': {'key': 'totalKeys', 'type': 'int'},
        'successful_keys': {'key': 'successfulKeys', 'type': 'int'},
        'failure_messages': {'key': 'failureMessages', 'type': '[str]'},
        'records': {'key': 'records', 'type': '[ResponseRecordStatus]'},
    }

    def __init__(self, **kwargs):
        super(PushUpdateStatusResponse, self).__init__(**kwargs)
        self.update_id = kwargs.get('update_id', None)
        self.status = kwargs.get('status', None)
        self.total_keys = kwargs.get('total_keys', None)
        self.successful_keys = kwargs.get('successful_keys', None)
        self.failure_messages = kwargs.get('failure_messages', None)
        self.records = kwargs.get('records', None)
