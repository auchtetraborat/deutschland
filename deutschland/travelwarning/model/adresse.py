"""
    Auswärtiges Amt OpenData Schnittstelle

    Dies ist die Beschreibung für die Schnittstelle zum Zugriff auf die Daten des [Auswärtigen Amtes](https://www.auswaertiges-amt.de/de/) im Rahmen der [OpenData](https://www.auswaertiges-amt.de/de/open-data-schnittstelle/736118) Initiative. ## Deaktivierung Die Schnittstelle kann deaktiviert werden, in dem Fall wird ein leeres JSON-Objekt zurückgegeben. ## Fehlerfall Im Fehlerfall wird ein leeres JSON-Objekt zurückgegeben. ## Nutzungsbedingungen Die Nutzungsbedingungen sind auf der [OpenData-Schnittstelle](https://www.auswaertiges-amt.de/de/open-data-schnittstelle/736118)  des Auswärtigen Amtes zu finden.   ## Änderungen ### version 1.0.1 (September 2021) * `content` (-> Details des Reise- und Sicherheitshinweis) wurde von [`/travelwarning`](#operations-default-getTravelwarning)  entfernt -> bitte ab jetzt [`/travelwarning/{contentId}`](#operations-default-getSingleTravelwarning) nutzen um `content` abzufragen  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.travelwarning.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from deutschland.travelwarning.exceptions import ApiAttributeError


class Adresse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "last_modified": (float,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "leader": (str,),  # noqa: E501
            "locales": (str,),  # noqa: E501
            "country": (str,),  # noqa: E501
            "zip": (str,),  # noqa: E501
            "city": (str,),  # noqa: E501
            "region": (str,),  # noqa: E501
            "street": (str,),  # noqa: E501
            "number": (str,),  # noqa: E501
            "departments": (str,),  # noqa: E501
            "fax": (str,),  # noqa: E501
            "telefone": (str,),  # noqa: E501
            "mail": (str,),  # noqa: E501
            "misc": (str,),  # noqa: E501
            "url": (str,),  # noqa: E501
            "postal": (str,),  # noqa: E501
            "type": (str,),  # noqa: E501
            "remark": (str,),  # noqa: E501
            "open": (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "last_modified": "lastModified",  # noqa: E501
        "title": "title",  # noqa: E501
        "leader": "leader",  # noqa: E501
        "locales": "locales",  # noqa: E501
        "country": "country",  # noqa: E501
        "zip": "zip",  # noqa: E501
        "city": "city",  # noqa: E501
        "region": "region",  # noqa: E501
        "street": "street",  # noqa: E501
        "number": "number",  # noqa: E501
        "departments": "departments",  # noqa: E501
        "fax": "fax",  # noqa: E501
        "telefone": "telefone",  # noqa: E501
        "mail": "mail",  # noqa: E501
        "misc": "misc",  # noqa: E501
        "url": "url",  # noqa: E501
        "postal": "postal",  # noqa: E501
        "type": "type",  # noqa: E501
        "remark": "remark",  # noqa: E501
        "open": "open",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Adresse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            last_modified (float): Zeitstempel der letzten Änderung. [optional]  # noqa: E501
            title (str): Titel. [optional]  # noqa: E501
            leader (str): Leiter. [optional]  # noqa: E501
            locales (str): Sprachen. [optional]  # noqa: E501
            country (str): Land. [optional]  # noqa: E501
            zip (str): Postleitzahl. [optional]  # noqa: E501
            city (str): Stadt. [optional]  # noqa: E501
            region (str): Region. [optional]  # noqa: E501
            street (str): Straße. [optional]  # noqa: E501
            number (str): Hausnummer. [optional]  # noqa: E501
            departments (str): Abteilungen. [optional]  # noqa: E501
            fax (str): Faxnummer. [optional]  # noqa: E501
            telefone (str): Telefonnummer. [optional]  # noqa: E501
            mail (str): E-Mail. [optional]  # noqa: E501
            misc (str): Sonstiges. [optional]  # noqa: E501
            url (str): Externer Link. [optional]  # noqa: E501
            postal (str): Postfach. [optional]  # noqa: E501
            type (str): Adresstyp. [optional]  # noqa: E501
            remark (str): Hinweis. [optional]  # noqa: E501
            open (str): Öffnungszeiten. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Adresse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            last_modified (float): Zeitstempel der letzten Änderung. [optional]  # noqa: E501
            title (str): Titel. [optional]  # noqa: E501
            leader (str): Leiter. [optional]  # noqa: E501
            locales (str): Sprachen. [optional]  # noqa: E501
            country (str): Land. [optional]  # noqa: E501
            zip (str): Postleitzahl. [optional]  # noqa: E501
            city (str): Stadt. [optional]  # noqa: E501
            region (str): Region. [optional]  # noqa: E501
            street (str): Straße. [optional]  # noqa: E501
            number (str): Hausnummer. [optional]  # noqa: E501
            departments (str): Abteilungen. [optional]  # noqa: E501
            fax (str): Faxnummer. [optional]  # noqa: E501
            telefone (str): Telefonnummer. [optional]  # noqa: E501
            mail (str): E-Mail. [optional]  # noqa: E501
            misc (str): Sonstiges. [optional]  # noqa: E501
            url (str): Externer Link. [optional]  # noqa: E501
            postal (str): Postfach. [optional]  # noqa: E501
            type (str): Adresstyp. [optional]  # noqa: E501
            remark (str): Hinweis. [optional]  # noqa: E501
            open (str): Öffnungszeiten. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
