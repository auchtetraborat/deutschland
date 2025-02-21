"""
    Bundesnetzagentur Strommarktdaten

    Bundesnetzagentur Strommarktdaten  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.smard.api_client import ApiClient, Endpoint as _Endpoint
from deutschland.smard.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from deutschland.smard.model.indices import Indices
from deutschland.smard.model.time_series import TimeSeries


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.filter_region_filter_copy_region_copy_resolution_timestamp_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (TimeSeries,),
                "auth": [],
                "endpoint_path": "/{filter}/{region}/{filterCopy}_{regionCopy}_{resolution}_{timestamp}.json",
                "operation_id": "filter_region_filter_copy_region_copy_resolution_timestamp_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "filter",
                    "filter_copy",
                    "region",
                    "region_copy",
                    "resolution",
                    "timestamp",
                ],
                "required": [
                    "filter",
                    "filter_copy",
                    "region",
                    "region_copy",
                    "resolution",
                    "timestamp",
                ],
                "nullable": [],
                "enum": [
                    "filter",
                    "filter_copy",
                    "region",
                    "region_copy",
                    "resolution",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("filter",): {
                        "1223": 1223,
                        "1224": 1224,
                        "1225": 1225,
                        "1226": 1226,
                        "1227": 1227,
                        "1228": 1228,
                        "4066": 4066,
                        "4067": 4067,
                        "4068": 4068,
                        "4069": 4069,
                        "4070": 4070,
                        "4071": 4071,
                        "410": 410,
                        "4359": 4359,
                        "4387": 4387,
                    },
                    ("filter_copy",): {
                        "1223": 1223,
                        "1224": 1224,
                        "1225": 1225,
                        "1226": 1226,
                        "1227": 1227,
                        "1228": 1228,
                        "4066": 4066,
                        "4067": 4067,
                        "4068": 4068,
                        "4069": 4069,
                        "4070": 4070,
                        "4071": 4071,
                        "410": 410,
                        "4359": 4359,
                        "4387": 4387,
                    },
                    ("region",): {
                        "DE": "DE",
                        "AT": "AT",
                        "LU": "LU",
                        "DE-LU": "DE-LU",
                        "DE-AT-LU": "DE-AT-LU",
                        "50HERTZ": "50Hertz",
                        "AMPRION": "Amprion",
                        "TENNET": "TenneT",
                        "TRANSNETBW": "TransnetBW",
                        "APG": "APG",
                        "CREOS": "Creos",
                    },
                    ("region_copy",): {
                        "DE": "DE",
                        "AT": "AT",
                        "LU": "LU",
                        "DE-LU": "DE-LU",
                        "DE-AT-LU": "DE-AT-LU",
                        "50HERTZ": "50Hertz",
                        "AMPRION": "Amprion",
                        "TENNET": "TenneT",
                        "TRANSNETBW": "TransnetBW",
                        "APG": "APG",
                        "CREOS": "Creos",
                    },
                    ("resolution",): {
                        "HOUR": "hour",
                        "QUARTERHOUR": "quarterhour",
                        "DAY": "day",
                        "WEEK": "week",
                        "MONTH": "month",
                        "YEAR": "year",
                    },
                },
                "openapi_types": {
                    "filter": (int,),
                    "filter_copy": (int,),
                    "region": (str,),
                    "region_copy": (str,),
                    "resolution": (str,),
                    "timestamp": (int,),
                },
                "attribute_map": {
                    "filter": "filter",
                    "filter_copy": "filterCopy",
                    "region": "region",
                    "region_copy": "regionCopy",
                    "resolution": "resolution",
                    "timestamp": "timestamp",
                },
                "location_map": {
                    "filter": "path",
                    "filter_copy": "path",
                    "region": "path",
                    "region_copy": "path",
                    "resolution": "path",
                    "timestamp": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.filter_region_index_resolution_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (Indices,),
                "auth": [],
                "endpoint_path": "/{filter}/{region}/index_{resolution}.json",
                "operation_id": "filter_region_index_resolution_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "filter",
                    "region",
                    "resolution",
                ],
                "required": [
                    "filter",
                    "region",
                    "resolution",
                ],
                "nullable": [],
                "enum": [
                    "filter",
                    "region",
                    "resolution",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("filter",): {
                        "1223": 1223,
                        "1224": 1224,
                        "1225": 1225,
                        "1226": 1226,
                        "1227": 1227,
                        "1228": 1228,
                        "4066": 4066,
                        "4067": 4067,
                        "4068": 4068,
                        "4069": 4069,
                        "4070": 4070,
                        "4071": 4071,
                        "410": 410,
                        "4359": 4359,
                        "4387": 4387,
                    },
                    ("region",): {
                        "DE": "DE",
                        "AT": "AT",
                        "LU": "LU",
                        "DE-LU": "DE-LU",
                        "DE-AT-LU": "DE-AT-LU",
                        "50HERTZ": "50Hertz",
                        "AMPRION": "Amprion",
                        "TENNET": "TenneT",
                        "TRANSNETBW": "TransnetBW",
                        "APG": "APG",
                        "CREOS": "Creos",
                    },
                    ("resolution",): {
                        "HOUR": "hour",
                        "QUARTERHOUR": "quarterhour",
                        "DAY": "day",
                        "WEEK": "week",
                        "MONTH": "month",
                        "YEAR": "year",
                    },
                },
                "openapi_types": {
                    "filter": (int,),
                    "region": (str,),
                    "resolution": (str,),
                },
                "attribute_map": {
                    "filter": "filter",
                    "region": "region",
                    "resolution": "resolution",
                },
                "location_map": {
                    "filter": "path",
                    "region": "path",
                    "resolution": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def filter_region_filter_copy_region_copy_resolution_timestamp_json_get(
        self,
        filter,
        filter_copy,
        region_copy,
        timestamp,
        region="DE",
        resolution="hour",
        **kwargs
    ):
        """Zeitreihendaten  # noqa: E501

        Zeitreihendaten nach Filter, Region und Auflösung ab Timestamp  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.filter_region_filter_copy_region_copy_resolution_timestamp_json_get(filter, filter_copy, region_copy, timestamp, region="DE", resolution="hour", async_req=True)
        >>> result = thread.get()

        Args:
            filter (int): Mögliche Filter:   * `1223` - Stromerzeugung: Braunkohle   * `1224` - Stromerzeugung: Kernenergie   * `1225` - Stromerzeugung: Wind Offshore   * `1226` - Stromerzeugung: Wasserkraft   * `1227` - Stromerzeugung: Sonstige Konventionelle   * `1228` - Stromerzeugung: Sonstige Erneuerbare   * `4066` - Stromerzeugung: Biomasse   * `4067` - Stromerzeugung: Wind Onshore   * `4068` - Stromerzeugung: Photovoltaik   * `4069` - Stromerzeugung: Steinkohle   * `4070` - Stromerzeugung: Pumpspeicher   * `4071` - Stromerzeugung: Erdgas   * `410` - Stromverbrauch: Gesamt (Netzlast)   * `4359` - Stromverbrauch: Residuallast   * `4387` - Stromverbrauch: Pumpspeicher
            filter_copy (int): Muss dem Wert von \"filter\" entsprechen. (Kaputtes API-Design)
            region_copy (str): Muss dem Wert von \"region\" entsprechen. (Kaputtes API-Design)
            timestamp (int):
            region (str): Land / Regelzone / Marktgebiet:   * `DE` - Land: Deutschland   * `AT` - Land: Österreich   * `LU` - Land: Luxemburg   * `DE-LU` - Marktgebiet: DE/LU (ab 01.10.2018)   * `DE-AT-LU` - Marktgebiet: DE/AT/LU (bis 30.09.2018)   * `50Hertz` - Regelzone (DE): 50Hertz   * `Amprion`- Regelzone (DE): Amprion   * `TenneT` - Regelzone (DE): TenneT   * `TransnetBW` - Regelzone (DE): TransnetBW   * `APG` - Regelzone (AT): APG   * `Creos` - Regelzone (LU): Creos . defaults to "DE", must be one of ["DE"]
            resolution (str): Auflösung der Daten:   * `hour` - Stündlich   * `quater_hour` - Viertelstündlich   * `day` - Täglich   * `week` - Wöchentlich   * `month` - Monatlich   * `year` - Jährlich . defaults to "hour", must be one of ["hour"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TimeSeries
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["filter"] = filter
        kwargs["filter_copy"] = filter_copy
        kwargs["region"] = region
        kwargs["region_copy"] = region_copy
        kwargs["resolution"] = resolution
        kwargs["timestamp"] = timestamp
        return self.filter_region_filter_copy_region_copy_resolution_timestamp_json_get_endpoint.call_with_http_info(
            **kwargs
        )

    def filter_region_index_resolution_json_get(
        self, filter, region="DE", resolution="hour", **kwargs
    ):
        """Indizes  # noqa: E501

        Verfügbare Timestamps für Filter, Region und Auflösung  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.filter_region_index_resolution_json_get(filter, region="DE", resolution="hour", async_req=True)
        >>> result = thread.get()

        Args:
            filter (int): Mögliche Filter:   * `1223` - Stromerzeugung: Braunkohle   * `1224` - Stromerzeugung: Kernenergie   * `1225` - Stromerzeugung: Wind Offshore   * `1226` - Stromerzeugung: Wasserkraft   * `1227` - Stromerzeugung: Sonstige Konventionelle   * `1228` - Stromerzeugung: Sonstige Erneuerbare   * `4066` - Stromerzeugung: Biomasse   * `4067` - Stromerzeugung: Wind Onshore   * `4068` - Stromerzeugung: Photovoltaik   * `4069` - Stromerzeugung: Steinkohle   * `4070` - Stromerzeugung: Pumpspeicher   * `4071` - Stromerzeugung: Erdgas   * `410` - Stromverbrauch: Gesamt (Netzlast)   * `4359` - Stromverbrauch: Residuallast   * `4387` - Stromverbrauch: Pumpspeicher
            region (str): Land / Regelzone / Marktgebiet:   * `DE` - Land: Deutschland   * `AT` - Land: Österreich   * `LU` - Land: Luxemburg   * `DE-LU` - Marktgebiet: DE/LU (ab 01.10.2018)   * `DE-AT-LU` - Marktgebiet: DE/AT/LU (bis 30.09.2018)   * `50Hertz` - Regelzone (DE): 50Hertz   * `Amprion`- Regelzone (DE): Amprion   * `TenneT` - Regelzone (DE): TenneT   * `TransnetBW` - Regelzone (DE): TransnetBW   * `APG` - Regelzone (AT): APG   * `Creos` - Regelzone (LU): Creos . defaults to "DE", must be one of ["DE"]
            resolution (str): Auflösung der Daten:   * `hour` - Stündlich   * `quater_hour` - Viertelstündlich   * `day` - Täglich   * `week` - Wöchentlich   * `month` - Monatlich   * `year` - Jährlich . defaults to "hour", must be one of ["hour"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Indices
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["filter"] = filter
        kwargs["region"] = region
        kwargs["resolution"] = resolution
        return (
            self.filter_region_index_resolution_json_get_endpoint.call_with_http_info(
                **kwargs
            )
        )
