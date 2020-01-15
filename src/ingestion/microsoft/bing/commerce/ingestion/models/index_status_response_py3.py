# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IndexStatusResponse(Model):
    """A response that represents the status of an index within its supported
    regions.

    :param index_statuses: A list of objects containing the status of the
     index within a region.
    :type index_statuses:
     list[~microsoft.bing.commerce.ingestion.models.ResponseIndexStatus]
    """

    _attribute_map = {
        'index_statuses': {'key': 'indexStatuses', 'type': '[ResponseIndexStatus]'},
    }

    def __init__(self, *, index_statuses=None, **kwargs) -> None:
        super(IndexStatusResponse, self).__init__(**kwargs)
        self.index_statuses = index_statuses
