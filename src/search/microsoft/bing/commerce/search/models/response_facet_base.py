# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_field_aggregation_base import ResponseFieldAggregationBase


class ResponseFacetBase(ResponseFieldAggregationBase):
    """ResponseFacetBase.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ResponseNumberFacet, ResponseStringFacet,
    ResponseCategoryFacet, ResponseBoolFacet, ResponseRangeFacet

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
    }

    _subtype_map = {
        '_type': {'NumberFacet': 'ResponseNumberFacet', 'StringFacet': 'ResponseStringFacet', 'CategoryFacet': 'ResponseCategoryFacet', 'BoolFacet': 'ResponseBoolFacet', 'RangeFacet': 'ResponseRangeFacet'}
    }

    def __init__(self, **kwargs):
        super(ResponseFacetBase, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self._type = 'Response.FacetBase'
