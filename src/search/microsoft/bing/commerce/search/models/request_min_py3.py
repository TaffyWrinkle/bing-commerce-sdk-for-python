# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .request_field_aggregation_base_py3 import RequestFieldAggregationBase


class RequestMin(RequestFieldAggregationBase):
    """Aggregation type for getting the min value of a field. Only applicable to
    numeric data.

    All required parameters must be populated in order to send to Azure.

    :param name: A label that you specify for your aggregations, which the API
     passes through and returns with the response.
    :type name: str
    :param aggregations: A list of child aggregations.
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.RequestAggregationBase]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param field: The field name.
    :type field: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aggregations': {'key': 'aggregations', 'type': '[RequestAggregationBase]'},
        '_type': {'key': '_type', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, aggregations=None, field: str=None, **kwargs) -> None:
        super(RequestMin, self).__init__(name=name, aggregations=aggregations, field=field, **kwargs)
        self._type = 'Min'
