# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .index_py3 import Index


class ResponseIndex(Index):
    """ResponseIndex.

    :param name: The index's name. The name must be unique per tenant, contain
     only ASCII characters, and have a maximum length of 64 characters.
    :type name: str
    :param description: A description of the index. The description is for the
     tenant's use. The description must contain only ASCII characters and have
     a maximum length of 64 characters.
    :type description: str
    :param regions: The array of regions where the customer data will be
     processed and served.
    :type regions: list[str or
     ~microsoft.bing.commerce.ingestion.models.Region]
    :param search_scenario: The type of search scenario that the user is using
     the index for, which includes Retail, Hotel, and Document. Possible values
     include: 'Unknown', 'Retail', 'Document', 'Hotel'. Default value: "Retail"
     .
    :type search_scenario: str or
     ~microsoft.bing.commerce.ingestion.models.enum
    :param search_services: The array of additional search services that the
     user wants to include for the index, which includes Autosuggest and
     VisualSearch.
    :type search_services: list[str]
    :param schema_version: The version for the schema of the index.
    :type schema_version: str
    :param fields: The fields that are associated with the index.
    :type fields: list[~microsoft.bing.commerce.ingestion.models.IndexField]
    :param id: The ID that uniquely identifies the index definition that had
     the CRUD operation applied.
    :type id: str
    :param provisioning_state: The current state of provisioning for the index
     definition. Possible values include: 'Unknown', 'NotStarted',
     'Provisioning', 'Deprovisioning', 'Succeeded', 'Failed'
    :type provisioning_state: str or
     ~microsoft.bing.commerce.ingestion.models.enum
    :param created_date_time: The date and time when the index was created.
    :type created_date_time: str
    """

    _validation = {
        'regions': {'unique': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'regions': {'key': 'regions', 'type': '[Region]'},
        'search_scenario': {'key': 'searchScenario', 'type': 'str'},
        'search_services': {'key': 'searchServices', 'type': '[str]'},
        'schema_version': {'key': 'schemaVersion', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '[IndexField]'},
        'id': {'key': 'id', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, description: str=None, regions=None, search_scenario="Retail", search_services=None, schema_version: str=None, fields=None, id: str=None, provisioning_state=None, created_date_time: str=None, **kwargs) -> None:
        super(ResponseIndex, self).__init__(name=name, description=description, regions=regions, search_scenario=search_scenario, search_services=search_services, schema_version=schema_version, fields=fields, **kwargs)
        self.id = id
        self.provisioning_state = provisioning_state
        self.created_date_time = created_date_time
