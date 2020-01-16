# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ResponsePushStatus(str, Enum):

    queued = "Queued"
    error = "Error"


class Region(str, Enum):

    unknown = "Unknown"
    east_asia = "EastAsia"
    east_us2 = "EastUS2"
    north_central_us = "NorthCentralUS"
    north_europe = "NorthEurope"
    west_us2 = "WestUS2"
    southeast_asia = "SoutheastAsia"
    australia_east = "AustraliaEast"
    australia_southeast = "AustraliaSoutheast"
    australia_central = "AustraliaCentral"
    australia_central2 = "AustraliaCentral2"
    brazil_south = "BrazilSouth"
    canada_central = "CanadaCentral"
    canada_east = "CanadaEast"
    china_north = "ChinaNorth"
    china_east = "ChinaEast"
    china_north2 = "ChinaNorth2"
    china_east2 = "ChinaEast2"
    west_europe = "WestEurope"
    france_central = "FranceCentral"
    france_south = "FranceSouth"
    germany_central = "GermanyCentral"
    germany_northeast = "GermanyNortheast"
    central_india = "CentralIndia"
    west_india = "WestIndia"
    south_india = "SouthIndia"
    japan_east = "JapanEast"
    japan_west = "JapanWest"
    korea_central = "KoreaCentral"
    korea_south = "KoreaSouth"
    east_us = "EastUS"
    west_us = "WestUS"
    central_us = "CentralUS"
    south_central_us = "SouthCentralUS"
    west_central_us = "WestCentralUS"
    south_africa_north = "SouthAfricaNorth"
    south_africa_west = "SouthAfricaWest"
    uk_west = "UKWest"
    uk_south = "UKSouth"
    uae_north = "UAENorth"
    uae_central = "UAECentral"


class IndexFieldType(str, Enum):

    unknown = "Unknown"
    string = "String"
    boolean = "Boolean"
    number = "Number"
    product_id = "ProductId"
    dup_id = "DupId"
    static_rank = "StaticRank"
    url = "Url"
    image_url = "ImageUrl"
    title = "Title"
    description = "Description"
    category = "Category"
    price = "Price"
    rating = "Rating"
    brand = "Brand"
    model = "Model"
    color = "Color"
    size = "Size"
    material = "Material"
    gender = "Gender"
    age_group = "AgeGroup"
    array = "Array"
    dictionary = "Dictionary"
    exclude_flag = "ExcludeFlag"
    identifier = "Identifier"
    object_enum = "Object"
    document_id = "DocumentId"
    author = "Author"
    created_at = "CreatedAt"
    modified_at = "ModifiedAt"
    paragraph = "Paragraph"
    sub_heading = "SubHeading"
    section_header = "SectionHeader"
    address = "Address"
    rating_count = "RatingCount"
    review_count = "ReviewCount"
    rating_scale = "RatingScale"
    amenities = "Amenities"
    street_address = "StreetAddress"
    locality = "Locality"
    sub_region = "SubRegion"
    address_region = "AddressRegion"
    postal_code = "PostalCode"
    post_office_box_number = "PostOfficeBoxNumber"
    country = "Country"
    country_iso = "CountryIso"
    neighborhood = "Neighborhood"
    other_areas = "OtherAreas"
    phone_number = "PhoneNumber"
    barcode = "Barcode"
    secondary_image_urls = "SecondaryImageUrls"
