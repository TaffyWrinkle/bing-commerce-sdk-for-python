# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RequestsStringSet(Model):
    """Defines a set of strings.

    :param values: A set of strings
    :type values: list[str]
    """

    _validation = {
        'values': {'unique': True},
    }

    _attribute_map = {
        'values': {'key': 'values', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(RequestsStringSet, self).__init__(**kwargs)
        self.values = kwargs.get('values', None)
