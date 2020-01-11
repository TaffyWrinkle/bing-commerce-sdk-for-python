# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .condition_base import ConditionBase


class ConditionBlock(ConditionBase):
    """Defines a list of composite conditions for filtering and boosting.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param conditions: The set of operands.
    :type conditions:
     list[~microsoft.bing.commerce.search.models.ConditionBase]
    :param operator: and, or. Default is `And`. Possible values include:
     'And', 'Or'
    :type operator: str or
     ~microsoft.bing.commerce.search.models.LogicalOperator
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'conditions': {'key': 'conditions', 'type': '[ConditionBase]'},
        'operator': {'key': 'operator', 'type': 'LogicalOperator'},
    }

    def __init__(self, **kwargs):
        super(ConditionBlock, self).__init__(**kwargs)
        self.conditions = kwargs.get('conditions', None)
        self.operator = kwargs.get('operator', None)
        self._type = 'ConditionBlock'
