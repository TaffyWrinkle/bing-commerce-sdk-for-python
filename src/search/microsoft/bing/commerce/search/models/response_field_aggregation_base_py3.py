# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_aggregation_py3 import ResponseAggregation


class ResponseFieldAggregationBase(ResponseAggregation):
    """Defines the abstract base type for aggregations based on fields.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ResponseFacetBase, ResponseMin, ResponseMax

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
    }

    _subtype_map = {
        '_type': {'Response.FacetBase': 'ResponseFacetBase', 'Min': 'ResponseMin', 'Max': 'ResponseMax'}
    }

    def __init__(self, *, errors=None, debug=None, name: str=None, estimated_count: int=None, aggregations=None, field: str=None, **kwargs) -> None:
        super(ResponseFieldAggregationBase, self).__init__(errors=errors, debug=debug, name=name, estimated_count=estimated_count, aggregations=aggregations, **kwargs)
        self.field = field
        self._type = 'Response.FieldAggregationBase'
