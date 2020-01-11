# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConditionBase(Model):
    """The condition that triggered a boost in ranking score.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ConditionBlock, FieldConditionBase, GeoCondition

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'ConditionBlock': 'ConditionBlock', 'FieldConditionBase': 'FieldConditionBase', 'GeoCondition': 'GeoCondition'}
    }

    def __init__(self, **kwargs):
        super(ConditionBase, self).__init__(**kwargs)
        self._type = None
