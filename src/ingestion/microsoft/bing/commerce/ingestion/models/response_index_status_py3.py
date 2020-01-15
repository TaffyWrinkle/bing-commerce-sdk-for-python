# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResponseIndexStatus(Model):
    """A response that represents a query to an index status within a region.

    :param region: Possible values include: 'Unknown', 'EastAsia', 'EastUS2',
     'NorthCentralUS', 'NorthEurope', 'WestUS2', 'SoutheastAsia',
     'AustraliaEast', 'AustraliaSoutheast', 'AustraliaCentral',
     'AustraliaCentral2', 'BrazilSouth', 'CanadaCentral', 'CanadaEast',
     'ChinaNorth', 'ChinaEast', 'ChinaNorth2', 'ChinaEast2', 'WestEurope',
     'FranceCentral', 'FranceSouth', 'GermanyCentral', 'GermanyNortheast',
     'CentralIndia', 'WestIndia', 'SouthIndia', 'JapanEast', 'JapanWest',
     'KoreaCentral', 'KoreaSouth', 'EastUS', 'WestUS', 'CentralUS',
     'SouthCentralUS', 'WestCentralUS', 'SouthAfricaNorth', 'SouthAfricaWest',
     'UKWest', 'UKSouth', 'UAENorth', 'UAECentral'
    :type region: str or ~microsoft.bing.commerce.ingestion.models.Region
    :param provisioning_state: The provisioning state for the index within the
     specified region. Possible values include: 'Unknown', 'NotStarted',
     'Provisioning', 'Deprovisioning', 'Succeeded', 'Failed'
    :type provisioning_state: str or
     ~microsoft.bing.commerce.ingestion.models.enum
    :param provisioning_percentage: The percentage of provisioning for the
     index withing the region.
    :type provisioning_percentage: float
    """

    _attribute_map = {
        'region': {'key': 'region', 'type': 'Region'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'provisioning_percentage': {'key': 'provisioningPercentage', 'type': 'float'},
    }

    def __init__(self, *, region=None, provisioning_state=None, provisioning_percentage: float=None, **kwargs) -> None:
        super(ResponseIndexStatus, self).__init__(**kwargs)
        self.region = region
        self.provisioning_state = provisioning_state
        self.provisioning_percentage = provisioning_percentage
