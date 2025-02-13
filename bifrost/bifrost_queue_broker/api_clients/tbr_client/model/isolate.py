"""
    SAP TBR Integration

    TBR integration for SAP  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from api_clients.tbr_client.model_utils import (  # noqa: F401
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


class Isolate(ModelNormal):
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

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

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
            'isolate_id': (str, none_type,),  # noqa: E501
            'test_date': (datetime, none_type,),  # noqa: E501
            'ssi_date': (datetime, none_type,),  # noqa: E501
            'cpr_nr': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'primary_isolate': (bool, none_type,),  # noqa: E501
            'kma_date': (datetime, none_type,),  # noqa: E501
            'kma_name': (str, none_type,),  # noqa: E501
            'gender': (str, none_type,),  # noqa: E501
            'age': (int, none_type,),  # noqa: E501
            'travel': (str, none_type,),  # noqa: E501
            'travel_country': (str, none_type,),  # noqa: E501
            'region': (str, none_type,),  # noqa: E501
            'run_id': (str, none_type,),  # noqa: E501
            'serotype': (str, none_type,),  # noqa: E501
            'st': (int, none_type,),  # noqa: E501
            'fud_nr': (str, none_type,),  # noqa: E501
            'cluster_id': (str, none_type,),  # noqa: E501
            'species': (str, none_type,),  # noqa: E501
            'subspecies': (str, none_type,),  # noqa: E501
            'pathotype': (str, none_type,),  # noqa: E501
            'adheasion': (str, none_type,),  # noqa: E501
            'toxin': (str, none_type,),  # noqa: E501
            'resistensgener': (str, none_type,),  # noqa: E501
            'amr_profile': (str, none_type,),  # noqa: E501
            'amikacin': (str, none_type,),  # noqa: E501
            'ampicillin': (str, none_type,),  # noqa: E501
            'azithromycin': (str, none_type,),  # noqa: E501
            'cefepime': (str, none_type,),  # noqa: E501
            'cefotaxime': (str, none_type,),  # noqa: E501
            'cefotaxime_clavulanat': (str, none_type,),  # noqa: E501
            'cefoxitin': (str, none_type,),  # noqa: E501
            'ceftazidime': (str, none_type,),  # noqa: E501
            'ceftazidime_clavulanat': (str, none_type,),  # noqa: E501
            'chloramphenicol': (str, none_type,),  # noqa: E501
            'ciprofloxacin': (str, none_type,),  # noqa: E501
            'clindamycin': (str, none_type,),  # noqa: E501
            'colistin': (str, none_type,),  # noqa: E501
            'daptomycin': (str, none_type,),  # noqa: E501
            'ertapenem': (str, none_type,),  # noqa: E501
            'erythromycin': (str, none_type,),  # noqa: E501
            'fusidinsyre': (str, none_type,),  # noqa: E501
            'gentamicin': (str, none_type,),  # noqa: E501
            'imipenem': (str, none_type,),  # noqa: E501
            'kanamycin': (str, none_type,),  # noqa: E501
            'linezolid': (str, none_type,),  # noqa: E501
            'meropenem': (str, none_type,),  # noqa: E501
            'mupirocin': (str, none_type,),  # noqa: E501
            'nalidixan': (str, none_type,),  # noqa: E501
            'penicillin': (str, none_type,),  # noqa: E501
            'ceftazidime_clavulanatn': (str, none_type,),  # noqa: E501
            'rifampin': (str, none_type,),  # noqa: E501
            'streptomycin': (str, none_type,),  # noqa: E501
            'sulfamethoxazole': (str, none_type,),  # noqa: E501
            'teicoplanin': (str, none_type,),  # noqa: E501
            'temocilin': (str, none_type,),  # noqa: E501
            'tetracyklin': (str, none_type,),  # noqa: E501
            'tiamulin': (str, none_type,),  # noqa: E501
            'tigecycline': (str, none_type,),  # noqa: E501
            'trimethoprim': (str, none_type,),  # noqa: E501
            'vancomycin': (str, none_type,),  # noqa: E501
            'resfinder_version': (str, none_type,),  # noqa: E501
            'date_approved_resistens': (datetime, none_type,),  # noqa: E501
            'date_approved_serotype': (datetime, none_type,),  # noqa: E501
            'date_approved_qc': (datetime, none_type,),  # noqa: E501
            'date_approved_st': (datetime, none_type,),  # noqa: E501
            'date_approved_toxin': (datetime, none_type,),  # noqa: E501
            'date_approved_cluster': (datetime, none_type,),  # noqa: E501
            'date_epi': (datetime, none_type,),  # noqa: E501
            'trst': (str, none_type,),  # noqa: E501
            'tcd_a': (str, none_type,),  # noqa: E501
            'tcd_b': (str, none_type,),  # noqa: E501
            'cdt_ab': (str, none_type,),  # noqa: E501
            'tcd_c_deletion': (str, none_type,),  # noqa: E501
            'tcd_c_117': (str, none_type,),  # noqa: E501
            'tcd_c_184_t': (str, none_type,),  # noqa: E501
            'tcd_c_a117_t': (str, none_type,),  # noqa: E501
            'row_ver': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'isolate_id': 'isolateId',  # noqa: E501
        'test_date': 'testDate',  # noqa: E501
        'ssi_date': 'ssiDate',  # noqa: E501
        'cpr_nr': 'cprNr',  # noqa: E501
        'name': 'name',  # noqa: E501
        'primary_isolate': 'primaryIsolate',  # noqa: E501
        'kma_date': 'kmaDate',  # noqa: E501
        'kma_name': 'kmaName',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'age': 'age',  # noqa: E501
        'travel': 'travel',  # noqa: E501
        'travel_country': 'travelCountry',  # noqa: E501
        'region': 'region',  # noqa: E501
        'run_id': 'runId',  # noqa: E501
        'serotype': 'serotype',  # noqa: E501
        'st': 'st',  # noqa: E501
        'fud_nr': 'fudNr',  # noqa: E501
        'cluster_id': 'clusterId',  # noqa: E501
        'species': 'species',  # noqa: E501
        'subspecies': 'subspecies',  # noqa: E501
        'pathotype': 'pathotype',  # noqa: E501
        'adheasion': 'adheasion',  # noqa: E501
        'toxin': 'toxin',  # noqa: E501
        'resistensgener': 'resistensgener',  # noqa: E501
        'amr_profile': 'amrProfile',  # noqa: E501
        'amikacin': 'amikacin',  # noqa: E501
        'ampicillin': 'ampicillin',  # noqa: E501
        'azithromycin': 'azithromycin',  # noqa: E501
        'cefepime': 'cefepime',  # noqa: E501
        'cefotaxime': 'cefotaxime',  # noqa: E501
        'cefotaxime_clavulanat': 'cefotaximeClavulanat',  # noqa: E501
        'cefoxitin': 'cefoxitin',  # noqa: E501
        'ceftazidime': 'ceftazidime',  # noqa: E501
        'ceftazidime_clavulanat': 'ceftazidimeClavulanat',  # noqa: E501
        'chloramphenicol': 'chloramphenicol',  # noqa: E501
        'ciprofloxacin': 'ciprofloxacin',  # noqa: E501
        'clindamycin': 'clindamycin',  # noqa: E501
        'colistin': 'colistin',  # noqa: E501
        'daptomycin': 'daptomycin',  # noqa: E501
        'ertapenem': 'ertapenem',  # noqa: E501
        'erythromycin': 'erythromycin',  # noqa: E501
        'fusidinsyre': 'fusidinsyre',  # noqa: E501
        'gentamicin': 'gentamicin',  # noqa: E501
        'imipenem': 'imipenem',  # noqa: E501
        'kanamycin': 'kanamycin',  # noqa: E501
        'linezolid': 'linezolid',  # noqa: E501
        'meropenem': 'meropenem',  # noqa: E501
        'mupirocin': 'mupirocin',  # noqa: E501
        'nalidixan': 'nalidixan',  # noqa: E501
        'penicillin': 'penicillin',  # noqa: E501
        'ceftazidime_clavulanatn': 'ceftazidimeClavulanatn',  # noqa: E501
        'rifampin': 'rifampin',  # noqa: E501
        'streptomycin': 'streptomycin',  # noqa: E501
        'sulfamethoxazole': 'sulfamethoxazole',  # noqa: E501
        'teicoplanin': 'teicoplanin',  # noqa: E501
        'temocilin': 'temocilin',  # noqa: E501
        'tetracyklin': 'tetracyklin',  # noqa: E501
        'tiamulin': 'tiamulin',  # noqa: E501
        'tigecycline': 'tigecycline',  # noqa: E501
        'trimethoprim': 'trimethoprim',  # noqa: E501
        'vancomycin': 'vancomycin',  # noqa: E501
        'resfinder_version': 'resfinderVersion',  # noqa: E501
        'date_approved_resistens': 'dateApprovedResistens',  # noqa: E501
        'date_approved_serotype': 'dateApprovedSerotype',  # noqa: E501
        'date_approved_qc': 'dateApprovedQC',  # noqa: E501
        'date_approved_st': 'dateApprovedST',  # noqa: E501
        'date_approved_toxin': 'dateApprovedToxin',  # noqa: E501
        'date_approved_cluster': 'dateApprovedCluster',  # noqa: E501
        'date_epi': 'dateEpi',  # noqa: E501
        'trst': 'trst',  # noqa: E501
        'tcd_a': 'tcdA',  # noqa: E501
        'tcd_b': 'tcdB',  # noqa: E501
        'cdt_ab': 'cdtAB',  # noqa: E501
        'tcd_c_deletion': 'tcdC_deletion',  # noqa: E501
        'tcd_c_117': 'tcdC_117',  # noqa: E501
        'tcd_c_184_t': 'tcdC_184T',  # noqa: E501
        'tcd_c_a117_t': 'tcdC_A117T',  # noqa: E501
        'row_ver': 'rowVer',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Isolate - a model defined in OpenAPI

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
            isolate_id (str, none_type): [optional]  # noqa: E501
            test_date (datetime, none_type): [optional]  # noqa: E501
            ssi_date (datetime, none_type): [optional]  # noqa: E501
            cpr_nr (str, none_type): [optional]  # noqa: E501
            name (str, none_type): [optional]  # noqa: E501
            primary_isolate (bool, none_type): [optional]  # noqa: E501
            kma_date (datetime, none_type): [optional]  # noqa: E501
            kma_name (str, none_type): [optional]  # noqa: E501
            gender (str, none_type): [optional]  # noqa: E501
            age (int, none_type): [optional]  # noqa: E501
            travel (str, none_type): [optional]  # noqa: E501
            travel_country (str, none_type): [optional]  # noqa: E501
            region (str, none_type): [optional]  # noqa: E501
            run_id (str, none_type): [optional]  # noqa: E501
            serotype (str, none_type): [optional]  # noqa: E501
            st (int, none_type): [optional]  # noqa: E501
            fud_nr (str, none_type): [optional]  # noqa: E501
            cluster_id (str, none_type): [optional]  # noqa: E501
            species (str, none_type): [optional]  # noqa: E501
            subspecies (str, none_type): [optional]  # noqa: E501
            pathotype (str, none_type): [optional]  # noqa: E501
            adheasion (str, none_type): [optional]  # noqa: E501
            toxin (str, none_type): [optional]  # noqa: E501
            resistensgener (str, none_type): [optional]  # noqa: E501
            amr_profile (str, none_type): [optional]  # noqa: E501
            amikacin (str, none_type): [optional]  # noqa: E501
            ampicillin (str, none_type): [optional]  # noqa: E501
            azithromycin (str, none_type): [optional]  # noqa: E501
            cefepime (str, none_type): [optional]  # noqa: E501
            cefotaxime (str, none_type): [optional]  # noqa: E501
            cefotaxime_clavulanat (str, none_type): [optional]  # noqa: E501
            cefoxitin (str, none_type): [optional]  # noqa: E501
            ceftazidime (str, none_type): [optional]  # noqa: E501
            ceftazidime_clavulanat (str, none_type): [optional]  # noqa: E501
            chloramphenicol (str, none_type): [optional]  # noqa: E501
            ciprofloxacin (str, none_type): [optional]  # noqa: E501
            clindamycin (str, none_type): [optional]  # noqa: E501
            colistin (str, none_type): [optional]  # noqa: E501
            daptomycin (str, none_type): [optional]  # noqa: E501
            ertapenem (str, none_type): [optional]  # noqa: E501
            erythromycin (str, none_type): [optional]  # noqa: E501
            fusidinsyre (str, none_type): [optional]  # noqa: E501
            gentamicin (str, none_type): [optional]  # noqa: E501
            imipenem (str, none_type): [optional]  # noqa: E501
            kanamycin (str, none_type): [optional]  # noqa: E501
            linezolid (str, none_type): [optional]  # noqa: E501
            meropenem (str, none_type): [optional]  # noqa: E501
            mupirocin (str, none_type): [optional]  # noqa: E501
            nalidixan (str, none_type): [optional]  # noqa: E501
            penicillin (str, none_type): [optional]  # noqa: E501
            ceftazidime_clavulanatn (str, none_type): [optional]  # noqa: E501
            rifampin (str, none_type): [optional]  # noqa: E501
            streptomycin (str, none_type): [optional]  # noqa: E501
            sulfamethoxazole (str, none_type): [optional]  # noqa: E501
            teicoplanin (str, none_type): [optional]  # noqa: E501
            temocilin (str, none_type): [optional]  # noqa: E501
            tetracyklin (str, none_type): [optional]  # noqa: E501
            tiamulin (str, none_type): [optional]  # noqa: E501
            tigecycline (str, none_type): [optional]  # noqa: E501
            trimethoprim (str, none_type): [optional]  # noqa: E501
            vancomycin (str, none_type): [optional]  # noqa: E501
            resfinder_version (str, none_type): [optional]  # noqa: E501
            date_approved_resistens (datetime, none_type): [optional]  # noqa: E501
            date_approved_serotype (datetime, none_type): [optional]  # noqa: E501
            date_approved_qc (datetime, none_type): [optional]  # noqa: E501
            date_approved_st (datetime, none_type): [optional]  # noqa: E501
            date_approved_toxin (datetime, none_type): [optional]  # noqa: E501
            date_approved_cluster (datetime, none_type): [optional]  # noqa: E501
            date_epi (datetime, none_type): [optional]  # noqa: E501
            trst (str, none_type): [optional]  # noqa: E501
            tcd_a (str, none_type): [optional]  # noqa: E501
            tcd_b (str, none_type): [optional]  # noqa: E501
            cdt_ab (str, none_type): [optional]  # noqa: E501
            tcd_c_deletion (str, none_type): [optional]  # noqa: E501
            tcd_c_117 (str, none_type): [optional]  # noqa: E501
            tcd_c_184_t (str, none_type): [optional]  # noqa: E501
            tcd_c_a117_t (str, none_type): [optional]  # noqa: E501
            row_ver (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
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
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
