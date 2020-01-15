# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SchemaDetectionResponse(Model):
    """SchemaDetectionResponse.

    :param index:
    :type index: ~microsoft.bing.commerce.ingestion.models.ResponseIndex
    :param transformation_config:
    :type transformation_config:
     ~microsoft.bing.commerce.ingestion.models.TransformationConfigResponse
    :param warnings:
    :type warnings: list[str]
    """

    _attribute_map = {
        'index': {'key': 'index', 'type': 'ResponseIndex'},
        'transformation_config': {'key': 'transformationConfig', 'type': 'TransformationConfigResponse'},
        'warnings': {'key': 'warnings', 'type': '[str]'},
    }

    def __init__(self, *, index=None, transformation_config=None, warnings=None, **kwargs) -> None:
        super(SchemaDetectionResponse, self).__init__(**kwargs)
        self.index = index
        self.transformation_config = transformation_config
        self.warnings = warnings
