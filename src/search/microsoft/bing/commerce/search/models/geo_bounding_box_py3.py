# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .geo_boundary_base_py3 import GeoBoundaryBase


class GeoBoundingBox(GeoBoundaryBase):
    """Defines a geographical box to match the results that lie within it.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :param top_left: The top-left corner geo-location of the box.
    :type top_left: ~microsoft.bing.commerce.search.models.GeoPoint
    :param bottom_right: The bottom-right corner geo-location of the box.
    :type bottom_right: ~microsoft.bing.commerce.search.models.GeoPoint
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'top_left': {'key': 'topLeft', 'type': 'GeoPoint'},
        'bottom_right': {'key': 'bottomRight', 'type': 'GeoPoint'},
    }

    def __init__(self, *, top_left=None, bottom_right=None, **kwargs) -> None:
        super(GeoBoundingBox, self).__init__(**kwargs)
        self.top_left = top_left
        self.bottom_right = bottom_right
        self._type = 'GeoBoundingBox'
