# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .request_match import RequestMatch


class RequestBingMatchStreams(RequestMatch):
    """RequestBingMatchStreams.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param value: The search terms to match on the specified fields.
    :type value: str
    :param include:
    :type include: list[str]
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'include': {'key': 'include', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(RequestBingMatchStreams, self).__init__(**kwargs)
        self.include = kwargs.get('include', None)
        self._type = 'MatchStreams'
