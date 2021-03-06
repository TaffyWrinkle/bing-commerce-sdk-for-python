# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_facet_base import ResponseFacetBase


class ResponseRangeFacet(ResponseFacetBase):
    """Defines a facet with a range refinement.

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
    :param label: The facet label, that you can use to render your UI.
    :type label: str
    :param refinements:
    :type refinements:
     list[~microsoft.bing.commerce.search.models.ResponseRangeRefinement]
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
        'label': {'key': 'label', 'type': 'str'},
        'refinements': {'key': 'refinements', 'type': '[ResponseRangeRefinement]'},
    }

    def __init__(self, **kwargs):
        super(ResponseRangeFacet, self).__init__(**kwargs)
        self.refinements = kwargs.get('refinements', None)
        self._type = 'RangeFacet'
