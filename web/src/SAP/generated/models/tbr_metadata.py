# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated.models.base_metadata import BaseMetadata
from web.src.SAP.generated.models.organization import Organization
from web.src.SAP.generated.models.tbr_specific_metadata import TbrSpecificMetadata
from web.src.SAP.generated import util

from web.src.SAP.generated.models.base_metadata import BaseMetadata  # noqa: E501
from web.src.SAP.generated.models.organization import Organization  # noqa: E501
from web.src.SAP.generated.models.tbr_specific_metadata import TbrSpecificMetadata  # noqa: E501

class TbrMetadata(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, sequence_id=None, sequence_filename=None, isolate_id=None, institution=None, project_number=None, project_title=None, sampling_date=None, received_date=None, sofi_date=None, run_id=None, public=None, primary_isolate=None, cpr_nr=None, gender=None, name=None, age=None, travel=None, travel_country=None, run_date=None, kma_received_date=None, kma=None, region=None, fud_number=None, cluster_id=None, epi_export=None):  # noqa: E501
        """TbrMetadata - a model defined in OpenAPI

        :param sequence_id: The sequence_id of this TbrMetadata.  # noqa: E501
        :type sequence_id: str
        :param sequence_filename: The sequence_filename of this TbrMetadata.  # noqa: E501
        :type sequence_filename: str
        :param isolate_id: The isolate_id of this TbrMetadata.  # noqa: E501
        :type isolate_id: str
        :param institution: The institution of this TbrMetadata.  # noqa: E501
        :type institution: Organization
        :param project_number: The project_number of this TbrMetadata.  # noqa: E501
        :type project_number: str
        :param project_title: The project_title of this TbrMetadata.  # noqa: E501
        :type project_title: str
        :param sampling_date: The sampling_date of this TbrMetadata.  # noqa: E501
        :type sampling_date: datetime
        :param received_date: The received_date of this TbrMetadata.  # noqa: E501
        :type received_date: datetime
        :param sofi_date: The sofi_date of this TbrMetadata.  # noqa: E501
        :type sofi_date: datetime
        :param run_id: The run_id of this TbrMetadata.  # noqa: E501
        :type run_id: str
        :param public: The public of this TbrMetadata.  # noqa: E501
        :type public: str
        :param primary_isolate: The primary_isolate of this TbrMetadata.  # noqa: E501
        :type primary_isolate: bool
        :param cpr_nr: The cpr_nr of this TbrMetadata.  # noqa: E501
        :type cpr_nr: str
        :param gender: The gender of this TbrMetadata.  # noqa: E501
        :type gender: str
        :param name: The name of this TbrMetadata.  # noqa: E501
        :type name: str
        :param age: The age of this TbrMetadata.  # noqa: E501
        :type age: int
        :param travel: The travel of this TbrMetadata.  # noqa: E501
        :type travel: str
        :param travel_country: The travel_country of this TbrMetadata.  # noqa: E501
        :type travel_country: str
        :param run_date: The run_date of this TbrMetadata.  # noqa: E501
        :type run_date: datetime
        :param kma_received_date: The kma_received_date of this TbrMetadata.  # noqa: E501
        :type kma_received_date: datetime
        :param kma: The kma of this TbrMetadata.  # noqa: E501
        :type kma: str
        :param region: The region of this TbrMetadata.  # noqa: E501
        :type region: str
        :param fud_number: The fud_number of this TbrMetadata.  # noqa: E501
        :type fud_number: str
        :param cluster_id: The cluster_id of this TbrMetadata.  # noqa: E501
        :type cluster_id: str
        :param epi_export: The epi_export of this TbrMetadata.  # noqa: E501
        :type epi_export: str
        """
        self.openapi_types = {
            'sequence_id': str,
            'sequence_filename': str,
            'isolate_id': str,
            'institution': Organization,
            'project_number': str,
            'project_title': str,
            'sampling_date': datetime,
            'received_date': datetime,
            'sofi_date': datetime,
            'run_id': str,
            'public': str,
            'primary_isolate': bool,
            'cpr_nr': str,
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
            'epi_export': str,
        }

        self.attribute_map = {
            'sequence_id': 'sequence_id',
            'sequence_filename': 'sequence_filename',
            'isolate_id': 'isolate_id',
            'institution': 'institution',
            'project_number': 'project_number',
            'project_title': 'project_title',
            'sampling_date': 'sampling_date',
            'received_date': 'received_date',
            'sofi_date': 'sofi_date',
            'run_id': 'run_id',
            'public': 'public',
            'primary_isolate': 'primary_isolate',
            'cpr_nr': 'cpr_nr',
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
            'epi_export': 'epi_export',
        }

        self._sequence_id = sequence_id
        self._sequence_filename = sequence_filename
        self._isolate_id = isolate_id
        self._institution = institution
        self._project_number = project_number
        self._project_title = project_title
        self._sampling_date = sampling_date
        self._received_date = received_date
        self._sofi_date = sofi_date
        self._run_id = run_id
        self._public = public
        self._primary_isolate = primary_isolate
        self._cpr_nr = cpr_nr
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
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TbrMetadata of this TbrMetadata.  # noqa: E501
        :rtype: TbrMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sequence_id(self):
        """Gets the sequence_id of this TbrMetadata.


        :return: The sequence_id of this TbrMetadata.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this TbrMetadata.


        :param sequence_id: The sequence_id of this TbrMetadata.
        :type sequence_id: str
        """
        if sequence_id is None:
            raise ValueError("Invalid value for `sequence_id`, must not be `None`")  # noqa: E501

        self._sequence_id = sequence_id

    @property
    def sequence_filename(self):
        """Gets the sequence_filename of this TbrMetadata.


        :return: The sequence_filename of this TbrMetadata.
        :rtype: str
        """
        return self._sequence_filename

    @sequence_filename.setter
    def sequence_filename(self, sequence_filename):
        """Sets the sequence_filename of this TbrMetadata.


        :param sequence_filename: The sequence_filename of this TbrMetadata.
        :type sequence_filename: str
        """

        self._sequence_filename = sequence_filename

    @property
    def isolate_id(self):
        """Gets the isolate_id of this TbrMetadata.


        :return: The isolate_id of this TbrMetadata.
        :rtype: str
        """
        return self._isolate_id

    @isolate_id.setter
    def isolate_id(self, isolate_id):
        """Sets the isolate_id of this TbrMetadata.


        :param isolate_id: The isolate_id of this TbrMetadata.
        :type isolate_id: str
        """
        if isolate_id is None:
            raise ValueError("Invalid value for `isolate_id`, must not be `None`")  # noqa: E501

        self._isolate_id = isolate_id

    @property
    def institution(self):
        """Gets the institution of this TbrMetadata.


        :return: The institution of this TbrMetadata.
        :rtype: Organization
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this TbrMetadata.


        :param institution: The institution of this TbrMetadata.
        :type institution: Organization
        """
        if institution is None:
            raise ValueError("Invalid value for `institution`, must not be `None`")  # noqa: E501

        self._institution = institution

    @property
    def project_number(self):
        """Gets the project_number of this TbrMetadata.


        :return: The project_number of this TbrMetadata.
        :rtype: str
        """
        return self._project_number

    @project_number.setter
    def project_number(self, project_number):
        """Sets the project_number of this TbrMetadata.


        :param project_number: The project_number of this TbrMetadata.
        :type project_number: str
        """

        self._project_number = project_number

    @property
    def project_title(self):
        """Gets the project_title of this TbrMetadata.


        :return: The project_title of this TbrMetadata.
        :rtype: str
        """
        return self._project_title

    @project_title.setter
    def project_title(self, project_title):
        """Sets the project_title of this TbrMetadata.


        :param project_title: The project_title of this TbrMetadata.
        :type project_title: str
        """

        self._project_title = project_title

    @property
    def sampling_date(self):
        """Gets the sampling_date of this TbrMetadata.


        :return: The sampling_date of this TbrMetadata.
        :rtype: datetime
        """
        return self._sampling_date

    @sampling_date.setter
    def sampling_date(self, sampling_date):
        """Sets the sampling_date of this TbrMetadata.


        :param sampling_date: The sampling_date of this TbrMetadata.
        :type sampling_date: datetime
        """

        self._sampling_date = sampling_date

    @property
    def received_date(self):
        """Gets the received_date of this TbrMetadata.


        :return: The received_date of this TbrMetadata.
        :rtype: datetime
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this TbrMetadata.


        :param received_date: The received_date of this TbrMetadata.
        :type received_date: datetime
        """
        if received_date is None:
            raise ValueError("Invalid value for `received_date`, must not be `None`")  # noqa: E501

        self._received_date = received_date

    @property
    def sofi_date(self):
        """Gets the sofi_date of this TbrMetadata.


        :return: The sofi_date of this TbrMetadata.
        :rtype: datetime
        """
        return self._sofi_date

    @sofi_date.setter
    def sofi_date(self, sofi_date):
        """Sets the sofi_date of this TbrMetadata.


        :param sofi_date: The sofi_date of this TbrMetadata.
        :type sofi_date: datetime
        """

        self._sofi_date = sofi_date

    @property
    def run_id(self):
        """Gets the run_id of this TbrMetadata.


        :return: The run_id of this TbrMetadata.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this TbrMetadata.


        :param run_id: The run_id of this TbrMetadata.
        :type run_id: str
        """
        if run_id is None:
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def public(self):
        """Gets the public of this TbrMetadata.


        :return: The public of this TbrMetadata.
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this TbrMetadata.


        :param public: The public of this TbrMetadata.
        :type public: str
        """

        self._public = public

    @property
    def primary_isolate(self):
        """Gets the primary_isolate of this TbrMetadata.


        :return: The primary_isolate of this TbrMetadata.
        :rtype: bool
        """
        return self._primary_isolate

    @primary_isolate.setter
    def primary_isolate(self, primary_isolate):
        """Sets the primary_isolate of this TbrMetadata.


        :param primary_isolate: The primary_isolate of this TbrMetadata.
        :type primary_isolate: bool
        """
        if primary_isolate is None:
            raise ValueError("Invalid value for `primary_isolate`, must not be `None`")  # noqa: E501

        self._primary_isolate = primary_isolate

    @property
    def cpr_nr(self):
        """Gets the cpr_nr of this TbrMetadata.


        :return: The cpr_nr of this TbrMetadata.
        :rtype: str
        """
        return self._cpr_nr

    @cpr_nr.setter
    def cpr_nr(self, cpr_nr):
        """Sets the cpr_nr of this TbrMetadata.


        :param cpr_nr: The cpr_nr of this TbrMetadata.
        :type cpr_nr: str
        """

        self._cpr_nr = cpr_nr

    @property
    def gender(self):
        """Gets the gender of this TbrMetadata.


        :return: The gender of this TbrMetadata.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this TbrMetadata.


        :param gender: The gender of this TbrMetadata.
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
        """Gets the name of this TbrMetadata.


        :return: The name of this TbrMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TbrMetadata.


        :param name: The name of this TbrMetadata.
        :type name: str
        """

        self._name = name

    @property
    def age(self):
        """Gets the age of this TbrMetadata.


        :return: The age of this TbrMetadata.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this TbrMetadata.


        :param age: The age of this TbrMetadata.
        :type age: int
        """
        if age is not None and age > 128:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value less than or equal to `128`")  # noqa: E501
        if age is not None and age < 0:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age = age

    @property
    def travel(self):
        """Gets the travel of this TbrMetadata.


        :return: The travel of this TbrMetadata.
        :rtype: str
        """
        return self._travel

    @travel.setter
    def travel(self, travel):
        """Sets the travel of this TbrMetadata.


        :param travel: The travel of this TbrMetadata.
        :type travel: str
        """

        self._travel = travel

    @property
    def travel_country(self):
        """Gets the travel_country of this TbrMetadata.


        :return: The travel_country of this TbrMetadata.
        :rtype: str
        """
        return self._travel_country

    @travel_country.setter
    def travel_country(self, travel_country):
        """Sets the travel_country of this TbrMetadata.


        :param travel_country: The travel_country of this TbrMetadata.
        :type travel_country: str
        """

        self._travel_country = travel_country

    @property
    def run_date(self):
        """Gets the run_date of this TbrMetadata.


        :return: The run_date of this TbrMetadata.
        :rtype: datetime
        """
        return self._run_date

    @run_date.setter
    def run_date(self, run_date):
        """Sets the run_date of this TbrMetadata.


        :param run_date: The run_date of this TbrMetadata.
        :type run_date: datetime
        """
        if run_date is None:
            raise ValueError("Invalid value for `run_date`, must not be `None`")  # noqa: E501

        self._run_date = run_date

    @property
    def kma_received_date(self):
        """Gets the kma_received_date of this TbrMetadata.


        :return: The kma_received_date of this TbrMetadata.
        :rtype: datetime
        """
        return self._kma_received_date

    @kma_received_date.setter
    def kma_received_date(self, kma_received_date):
        """Sets the kma_received_date of this TbrMetadata.


        :param kma_received_date: The kma_received_date of this TbrMetadata.
        :type kma_received_date: datetime
        """

        self._kma_received_date = kma_received_date

    @property
    def kma(self):
        """Gets the kma of this TbrMetadata.


        :return: The kma of this TbrMetadata.
        :rtype: str
        """
        return self._kma

    @kma.setter
    def kma(self, kma):
        """Sets the kma of this TbrMetadata.


        :param kma: The kma of this TbrMetadata.
        :type kma: str
        """

        self._kma = kma

    @property
    def region(self):
        """Gets the region of this TbrMetadata.


        :return: The region of this TbrMetadata.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TbrMetadata.


        :param region: The region of this TbrMetadata.
        :type region: str
        """

        self._region = region

    @property
    def fud_number(self):
        """Gets the fud_number of this TbrMetadata.


        :return: The fud_number of this TbrMetadata.
        :rtype: str
        """
        return self._fud_number

    @fud_number.setter
    def fud_number(self, fud_number):
        """Sets the fud_number of this TbrMetadata.


        :param fud_number: The fud_number of this TbrMetadata.
        :type fud_number: str
        """

        self._fud_number = fud_number

    @property
    def cluster_id(self):
        """Gets the cluster_id of this TbrMetadata.


        :return: The cluster_id of this TbrMetadata.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this TbrMetadata.


        :param cluster_id: The cluster_id of this TbrMetadata.
        :type cluster_id: str
        """

        self._cluster_id = cluster_id

    @property
    def epi_export(self):
        """Gets the epi_export of this TbrMetadata.


        :return: The epi_export of this TbrMetadata.
        :rtype: str
        """
        return self._epi_export

    @epi_export.setter
    def epi_export(self, epi_export):
        """Sets the epi_export of this TbrMetadata.


        :param epi_export: The epi_export of this TbrMetadata.
        :type epi_export: str
        """

        self._epi_export = epi_export
