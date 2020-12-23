# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
import re
from .. import util

import re  # noqa: E501

class TbrSpecificMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cpr=None, gender=None, name=None, age=None, travel=None, travel_country=None, run_date=None, kma_received_date=None, kma=None, region=None, fud_number=None, cluster_id=None, epi_export=None):  # noqa: E501
        """TbrSpecificMetadata - a model defined in OpenAPI

        :param cpr: The cpr of this TbrSpecificMetadata.  # noqa: E501
        :type cpr: str
        :param gender: The gender of this TbrSpecificMetadata.  # noqa: E501
        :type gender: str
        :param name: The name of this TbrSpecificMetadata.  # noqa: E501
        :type name: str
        :param age: The age of this TbrSpecificMetadata.  # noqa: E501
        :type age: int
        :param travel: The travel of this TbrSpecificMetadata.  # noqa: E501
        :type travel: str
        :param travel_country: The travel_country of this TbrSpecificMetadata.  # noqa: E501
        :type travel_country: str
        :param run_date: The run_date of this TbrSpecificMetadata.  # noqa: E501
        :type run_date: datetime
        :param kma_received_date: The kma_received_date of this TbrSpecificMetadata.  # noqa: E501
        :type kma_received_date: datetime
        :param kma: The kma of this TbrSpecificMetadata.  # noqa: E501
        :type kma: str
        :param region: The region of this TbrSpecificMetadata.  # noqa: E501
        :type region: str
        :param fud_number: The fud_number of this TbrSpecificMetadata.  # noqa: E501
        :type fud_number: str
        :param cluster_id: The cluster_id of this TbrSpecificMetadata.  # noqa: E501
        :type cluster_id: str
        :param epi_export: The epi_export of this TbrSpecificMetadata.  # noqa: E501
        :type epi_export: str
        """
        self.openapi_types = {
            'cpr': str,
            'gender': str,
            'name': str,
            'age': int,
            'travel': str,
            'travel_country': str,
            'run_date': datetime,
            'kma_received_date': datetime,
            'kma': str,
            'region': str,
            'fud_number': str,
            'cluster_id': str,
            'epi_export': str
        }

        self.attribute_map = {
            'cpr': 'cpr',
            'gender': 'gender',
            'name': 'name',
            'age': 'age',
            'travel': 'travel',
            'travel_country': 'travel_country',
            'run_date': 'run_date',
            'kma_received_date': 'kma_received_date',
            'kma': 'kma',
            'region': 'region',
            'fud_number': 'fud_number',
            'cluster_id': 'cluster_id',
            'epi_export': 'epi_export'
        }

        self._cpr = cpr
        self._gender = gender
        self._name = name
        self._age = age
        self._travel = travel
        self._travel_country = travel_country
        self._run_date = run_date
        self._kma_received_date = kma_received_date
        self._kma = kma
        self._region = region
        self._fud_number = fud_number
        self._cluster_id = cluster_id
        self._epi_export = epi_export

    @classmethod
    def from_dict(cls, dikt) -> 'TbrSpecificMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TbrSpecificMetadata of this TbrSpecificMetadata.  # noqa: E501
        :rtype: TbrSpecificMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cpr(self):
        """Gets the cpr of this TbrSpecificMetadata.


        :return: The cpr of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._cpr

    @cpr.setter
    def cpr(self, cpr):
        """Sets the cpr of this TbrSpecificMetadata.


        :param cpr: The cpr of this TbrSpecificMetadata.
        :type cpr: str
        """
        if cpr is not None and not re.search(r'^(?:(?:31(?:0[13578]|1[02])|(?:30|29)(?:0[13-9]|1[0-2])|(?:0[1-9]|1[0-9]|2[0-8])(?:0[1-9]|1[0-2]))[0-9]{2}\s?-?\s?[0-9]|290200\s-?\s[4-9]|2902(?:(?!00)[02468][048]|[13579][26])\s?-?\s?[0-3])[0-9]{3}|000000\s?-?\s?0000$', cpr):  # noqa: E501
            raise ValueError("Invalid value for `cpr`, must be a follow pattern or equal to `/^(?:(?:31(?:0[13578]|1[02])|(?:30|29)(?:0[13-9]|1[0-2])|(?:0[1-9]|1[0-9]|2[0-8])(?:0[1-9]|1[0-2]))[0-9]{2}\s?-?\s?[0-9]|290200\s-?\s[4-9]|2902(?:(?!00)[02468][048]|[13579][26])\s?-?\s?[0-3])[0-9]{3}|000000\s?-?\s?0000$/`")  # noqa: E501

        self._cpr = cpr

    @property
    def gender(self):
        """Gets the gender of this TbrSpecificMetadata.


        :return: The gender of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this TbrSpecificMetadata.


        :param gender: The gender of this TbrSpecificMetadata.
        :type gender: str
        """
        allowed_values = ["M", "K"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def name(self):
        """Gets the name of this TbrSpecificMetadata.


        :return: The name of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TbrSpecificMetadata.


        :param name: The name of this TbrSpecificMetadata.
        :type name: str
        """

        self._name = name

    @property
    def age(self):
        """Gets the age of this TbrSpecificMetadata.


        :return: The age of this TbrSpecificMetadata.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this TbrSpecificMetadata.


        :param age: The age of this TbrSpecificMetadata.
        :type age: int
        """
        if age is not None and age > 128:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value less than or equal to `128`")  # noqa: E501
        if age is not None and age < 0:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age = age

    @property
    def travel(self):
        """Gets the travel of this TbrSpecificMetadata.


        :return: The travel of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._travel

    @travel.setter
    def travel(self, travel):
        """Sets the travel of this TbrSpecificMetadata.


        :param travel: The travel of this TbrSpecificMetadata.
        :type travel: str
        """

        self._travel = travel

    @property
    def travel_country(self):
        """Gets the travel_country of this TbrSpecificMetadata.


        :return: The travel_country of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._travel_country

    @travel_country.setter
    def travel_country(self, travel_country):
        """Sets the travel_country of this TbrSpecificMetadata.


        :param travel_country: The travel_country of this TbrSpecificMetadata.
        :type travel_country: str
        """

        self._travel_country = travel_country

    @property
    def run_date(self):
        """Gets the run_date of this TbrSpecificMetadata.


        :return: The run_date of this TbrSpecificMetadata.
        :rtype: datetime
        """
        return self._run_date

    @run_date.setter
    def run_date(self, run_date):
        """Sets the run_date of this TbrSpecificMetadata.


        :param run_date: The run_date of this TbrSpecificMetadata.
        :type run_date: datetime
        """
        if run_date is None:
            raise ValueError("Invalid value for `run_date`, must not be `None`")  # noqa: E501

        self._run_date = run_date

    @property
    def kma_received_date(self):
        """Gets the kma_received_date of this TbrSpecificMetadata.


        :return: The kma_received_date of this TbrSpecificMetadata.
        :rtype: datetime
        """
        return self._kma_received_date

    @kma_received_date.setter
    def kma_received_date(self, kma_received_date):
        """Sets the kma_received_date of this TbrSpecificMetadata.


        :param kma_received_date: The kma_received_date of this TbrSpecificMetadata.
        :type kma_received_date: datetime
        """

        self._kma_received_date = kma_received_date

    @property
    def kma(self):
        """Gets the kma of this TbrSpecificMetadata.


        :return: The kma of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._kma

    @kma.setter
    def kma(self, kma):
        """Sets the kma of this TbrSpecificMetadata.


        :param kma: The kma of this TbrSpecificMetadata.
        :type kma: str
        """

        self._kma = kma

    @property
    def region(self):
        """Gets the region of this TbrSpecificMetadata.


        :return: The region of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TbrSpecificMetadata.


        :param region: The region of this TbrSpecificMetadata.
        :type region: str
        """

        self._region = region

    @property
    def fud_number(self):
        """Gets the fud_number of this TbrSpecificMetadata.


        :return: The fud_number of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._fud_number

    @fud_number.setter
    def fud_number(self, fud_number):
        """Sets the fud_number of this TbrSpecificMetadata.


        :param fud_number: The fud_number of this TbrSpecificMetadata.
        :type fud_number: str
        """

        self._fud_number = fud_number

    @property
    def cluster_id(self):
        """Gets the cluster_id of this TbrSpecificMetadata.


        :return: The cluster_id of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this TbrSpecificMetadata.


        :param cluster_id: The cluster_id of this TbrSpecificMetadata.
        :type cluster_id: str
        """

        self._cluster_id = cluster_id

    @property
    def epi_export(self):
        """Gets the epi_export of this TbrSpecificMetadata.


        :return: The epi_export of this TbrSpecificMetadata.
        :rtype: str
        """
        return self._epi_export

    @epi_export.setter
    def epi_export(self, epi_export):
        """Sets the epi_export of this TbrSpecificMetadata.


        :param epi_export: The epi_export of this TbrSpecificMetadata.
        :type epi_export: str
        """

        self._epi_export = epi_export
