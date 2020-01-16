# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .request_aggregation_base import RequestAggregationBase


class RequestDiscoverFacets(RequestAggregationBase):
    """Defines an aggregation type that triggers facet discovery of significant
    facets.

    All required parameters must be populated in order to send to Azure.

    :param name: A label that you specify for your aggregations, which the API
     passes through and returns with the response.
    :type name: str
    :param aggregations: A list of child aggregations.
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.RequestAggregationBase]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param discover_filter: When true, if the top results share a filter then
     restrict facet discovery to that filter. Note that it attempts to discover
     category based filters. Default value: False .
    :type discover_filter: bool
    :param refinements: When true, returns refinement values in the response.
     Default value: True .
    :type refinements: bool
    :param pin: A list of facets to pin at the top positions of the
     DiscoveredFacets aggregations list.
    :type pin: list[~microsoft.bing.commerce.search.models.RequestFacetBase]
    :param include: A list of facets to be included, but not necessarily at
     the top positions.
    :type include:
     list[~microsoft.bing.commerce.search.models.RequestFacetBase]
    :param exclude: A list of field names to exclude from consideration.
    :type exclude: list[str]
    :param facet_defaults: default facets to apply.
    :type facet_defaults: ~microsoft.bing.commerce.search.models.RequestFacet
    :param range_facet_defaults: default range facets to apply.
    :type range_facet_defaults:
     ~microsoft.bing.commerce.search.models.RequestRangeFacet
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aggregations': {'key': 'aggregations', 'type': '[RequestAggregationBase]'},
        '_type': {'key': '_type', 'type': 'str'},
        'discover_filter': {'key': 'discoverFilter', 'type': 'bool'},
        'refinements': {'key': 'refinements', 'type': 'bool'},
        'pin': {'key': 'pin', 'type': '[RequestFacetBase]'},
        'include': {'key': 'include', 'type': '[RequestFacetBase]'},
        'exclude': {'key': 'exclude', 'type': '[str]'},
        'facet_defaults': {'key': 'facetDefaults', 'type': 'RequestFacet'},
        'range_facet_defaults': {'key': 'rangeFacetDefaults', 'type': 'RequestRangeFacet'},
    }

    def __init__(self, **kwargs):
        super(RequestDiscoverFacets, self).__init__(**kwargs)
        self.discover_filter = kwargs.get('discover_filter', False)
        self.refinements = kwargs.get('refinements', True)
        self.pin = kwargs.get('pin', None)
        self.include = kwargs.get('include', None)
        self.exclude = kwargs.get('exclude', None)
        self.facet_defaults = kwargs.get('facet_defaults', None)
        self.range_facet_defaults = kwargs.get('range_facet_defaults', None)
        self._type = 'DiscoverFacets'
