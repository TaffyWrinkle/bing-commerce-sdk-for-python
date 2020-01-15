# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Index(Model):
    """Contains the definition for the index. An index consists of a set of
    documents that search operations can be performed upon.

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
    }

    def __init__(self, *, name: str=None, description: str=None, regions=None, search_scenario="Retail", search_services=None, schema_version: str=None, fields=None, **kwargs) -> None:
        super(Index, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.regions = regions
        self.search_scenario = search_scenario
        self.search_services = search_services
        self.schema_version = schema_version
        self.fields = fields
