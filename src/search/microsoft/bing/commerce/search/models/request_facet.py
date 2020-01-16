# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .request_facet_base import RequestFacetBase


class RequestFacet(RequestFacetBase):
    """Defines a facet where each refinement is for a single value.

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
    :param order_by: A comma-separated list of OData order syntax expressions.
     Default is `_count desc`
    :type order_by: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aggregations': {'key': 'aggregations', 'type': '[RequestAggregationBase]'},
        '_type': {'key': '_type', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
        'order_by': {'key': 'orderBy', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RequestFacet, self).__init__(**kwargs)
        self._type = 'Facet'
