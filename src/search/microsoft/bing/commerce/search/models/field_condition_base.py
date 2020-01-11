# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .condition_base import ConditionBase


class FieldConditionBase(ConditionBase):
    """Defines the abstract base type for conditions with a field name.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: EquivalenceConditionBase, NumericCondition,
    CategoryCondition, SetConditionBase

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param field: The name of the field.
    :type field: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'EquivalenceConditionBase': 'EquivalenceConditionBase', 'NumericCondition': 'NumericCondition', 'CategoryCondition': 'CategoryCondition', 'SetConditionBase': 'SetConditionBase'}
    }

    def __init__(self, **kwargs):
        super(FieldConditionBase, self).__init__(**kwargs)
        self.field = kwargs.get('field', None)
        self._type = 'FieldConditionBase'
