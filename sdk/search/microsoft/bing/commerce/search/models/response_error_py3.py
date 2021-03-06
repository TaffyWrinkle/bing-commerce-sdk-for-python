# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResponseError(Model):
    """Defines The error details that happened to a task.

    :param code: Possible values include: 'None', 'ServerError',
     'InvalidRequest', 'InsufficientAuthorization'. Default value: "None" .
    :type code: str or ~microsoft.bing.commerce.search.models.enum
    :param sub_code: Possible values include: 'UnexpectedError',
     'ResourceError', 'DeadlineExceeded', 'ParameterMissing',
     'ParameterInvalidValue'
    :type sub_code: str or ~microsoft.bing.commerce.search.models.enum
    :param message:
    :type message: str
    :param more_details:
    :type more_details: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'sub_code': {'key': 'subCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'more_details': {'key': 'moreDetails', 'type': 'str'},
    }

    def __init__(self, *, code="None", sub_code=None, message: str=None, more_details: str=None, **kwargs) -> None:
        super(ResponseError, self).__init__(**kwargs)
        self.code = code
        self.sub_code = sub_code
        self.message = message
        self.more_details = more_details
