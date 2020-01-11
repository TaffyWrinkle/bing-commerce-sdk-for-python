# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .set_condition_base import SetConditionBase


class StringSetCondition(SetConditionBase):
    """Defines a condition where the field must exactly match one of the values
    within the set to be included / excluded. It can appear in a filter, a
    boost, or a filter aggregation.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param field: The name of the field.
    :type field: str
    :param operator: Possible values include: 'In', 'NotIn'
    :type operator: str or ~microsoft.bing.commerce.search.models.SetOperator
    :param values: The set of values for the field to match against.
    :type values: list[str]
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'SetOperator'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(StringSetCondition, self).__init__(**kwargs)
        self.values = kwargs.get('values', None)
        self._type = 'StringSetCondition'