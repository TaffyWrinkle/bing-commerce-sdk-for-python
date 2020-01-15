# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .request_query_clause_base_py3 import RequestQueryClauseBase


class RequestMatch(RequestQueryClauseBase):
    """Defines a type of query to search specific fields.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: RequestBingMatchStreams

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param value: The search terms to match on the specified fields.
    :type value: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'MatchStreams': 'RequestBingMatchStreams'}
    }

    def __init__(self, *, value: str=None, **kwargs) -> None:
        super(RequestMatch, self).__init__(**kwargs)
        self.value = value
        self._type = 'Match'
