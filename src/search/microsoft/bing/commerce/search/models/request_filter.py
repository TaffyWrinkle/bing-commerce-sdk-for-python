# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .request_aggregation_base import RequestAggregationBase


class RequestFilter(RequestAggregationBase):
    """Defines a filter aggregation.

    All required parameters must be populated in order to send to Azure.

    :param name: A label that you specify for your aggregations, which the API
     passes through and returns with the response.
    :type name: str
    :param aggregations: A list of child aggregations.
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.RequestAggregationBase]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param value: The condition to match for the aggregation.
    :type value: ~microsoft.bing.commerce.search.models.ConditionBase
    :param include_customizations:  Default value: True .
    :type include_customizations: bool
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aggregations': {'key': 'aggregations', 'type': '[RequestAggregationBase]'},
        '_type': {'key': '_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'ConditionBase'},
        'include_customizations': {'key': 'includeCustomizations', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(RequestFilter, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.include_customizations = kwargs.get('include_customizations', True)
        self._type = 'Filter'
