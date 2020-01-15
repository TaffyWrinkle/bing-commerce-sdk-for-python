# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_items_base_py3 import ResponseItemsBase


class ResponseItems(ResponseItemsBase):
    """Defines a list of items from the result set.

    All required parameters must be populated in order to send to Azure.

    :param errors: A list of errors that happened to the task, if any.
    :type errors: list[~microsoft.bing.commerce.search.models.ResponseError]
    :param debug:
    :type debug:
     list[~microsoft.bing.commerce.search.models.ResponseDebugInfo]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param total_estimated_matches: An estimated count of the items in the
     full result set.
    :type total_estimated_matches: long
    :param value: The item results. May be limited by pagination.
    :type value: list[~microsoft.bing.commerce.search.models.ResponseItem]
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ResponseError]'},
        'debug': {'key': 'debug', 'type': '[ResponseDebugInfo]'},
        '_type': {'key': '_type', 'type': 'str'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'value': {'key': 'value', 'type': '[ResponseItem]'},
    }

    def __init__(self, *, errors=None, debug=None, total_estimated_matches: int=None, value=None, **kwargs) -> None:
        super(ResponseItems, self).__init__(errors=errors, debug=debug, total_estimated_matches=total_estimated_matches, **kwargs)
        self.value = value
        self._type = 'Items'
