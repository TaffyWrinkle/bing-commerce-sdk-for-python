# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .equivalence_condition_base import EquivalenceConditionBase


class BoolCondition(EquivalenceConditionBase):
    """Defines an equivalence condition for a Boolean field. It can appear in a
    filter, a boost, or a filter aggregation.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param field: The name of the field.
    :type field: str
    :param operator: Possible values include: 'Eq', 'Ne'
    :type operator: str or
     ~microsoft.bing.commerce.search.models.EquivalenceOperator
    :param value: The value (true or false) to compare the field against.
    :type value: bool
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'EquivalenceOperator'},
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(BoolCondition, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self._type = 'BoolCondition'