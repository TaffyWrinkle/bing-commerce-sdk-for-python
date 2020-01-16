# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_field_aggregation_base_py3 import ResponseFieldAggregationBase


class ResponseMax(ResponseFieldAggregationBase):
    """Returns the maximum value of the field encountered within the match set.

    All required parameters must be populated in order to send to Azure.

    :param errors: A list of errors that happened to the task, if any.
    :type errors: list[~microsoft.bing.commerce.search.models.ResponseError]
    :param debug:
    :type debug:
     list[~microsoft.bing.commerce.search.models.ResponseDebugInfo]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param name: The aggregation name as defined in the requset.
    :type name: str
    :param estimated_count: An estimated count of items in this aggregation.
    :type estimated_count: long
    :param aggregations: The list of child aggregations, if any.
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.ResponseAggregation]
    :param field: The name of the field.
    :type field: str
    :param value: The maximum value of the field for the match set.
    :type value: float
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ResponseError]'},
        'debug': {'key': 'debug', 'type': '[ResponseDebugInfo]'},
        '_type': {'key': '_type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'estimated_count': {'key': 'estimatedCount', 'type': 'long'},
        'aggregations': {'key': 'aggregations', 'type': '[ResponseAggregation]'},
        'field': {'key': 'field', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, *, errors=None, debug=None, name: str=None, estimated_count: int=None, aggregations=None, field: str=None, value: float=None, **kwargs) -> None:
        super(ResponseMax, self).__init__(errors=errors, debug=debug, name=name, estimated_count=estimated_count, aggregations=aggregations, field=field, **kwargs)
        self.value = value
        self._type = 'Max'
