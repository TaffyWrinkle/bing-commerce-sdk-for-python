# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_task_py3 import ResponseTask


class ResponseQueryContext(ResponseTask):
    """Defines an object that contains the result of query alteration.

    All required parameters must be populated in order to send to Azure.

    :param errors: A list of errors that happened to the task, if any.
    :type errors: list[~microsoft.bing.commerce.search.models.ResponseError]
    :param debug:
    :type debug:
     list[~microsoft.bing.commerce.search.models.ResponseDebugInfo]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param original_query: The user's query string as entered.
    :type original_query: str
    :param altered_query: The altered query string that the API actually uses
     for the query (for example, corrected spelling).
    :type altered_query: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ResponseError]'},
        'debug': {'key': 'debug', 'type': '[ResponseDebugInfo]'},
        '_type': {'key': '_type', 'type': 'str'},
        'original_query': {'key': 'originalQuery', 'type': 'str'},
        'altered_query': {'key': 'alteredQuery', 'type': 'str'},
    }

    def __init__(self, *, errors=None, debug=None, original_query: str=None, altered_query: str=None, **kwargs) -> None:
        super(ResponseQueryContext, self).__init__(errors=errors, debug=debug, **kwargs)
        self.original_query = original_query
        self.altered_query = altered_query
        self._type = 'Response.QueryContext'