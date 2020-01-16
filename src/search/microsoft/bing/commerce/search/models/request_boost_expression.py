# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RequestBoostExpression(Model):
    """Defines an expression that modifies the ranking score of results based on a
    condition.

    :param condition: The condition that triggers a boost in ranking score.
    :type condition: ~microsoft.bing.commerce.search.models.ConditionBase
    :param boost: The magnitude of a boost. The range is -10 million to 10
     million.
    :type boost: float
    """

    _attribute_map = {
        'condition': {'key': 'condition', 'type': 'ConditionBase'},
        'boost': {'key': 'boost', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(RequestBoostExpression, self).__init__(**kwargs)
        self.condition = kwargs.get('condition', None)
        self.boost = kwargs.get('boost', None)
