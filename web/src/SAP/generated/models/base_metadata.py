# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated.models.organization import Organization
from web.src.SAP.generated import util

from web.src.SAP.generated.models.organization import Organization  # noqa: E501

class BaseMetadata(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, sequence_id=None, sequence_filename=None, isolate_id=None, institution=None, project_number=None, project_title=None, sampling_date=None, received_date=None, sofi_date=None, run_id=None, public=None, primary_isolate=None):  # noqa: E501
        """BaseMetadata - a model defined in OpenAPI

        :param sequence_id: The sequence_id of this BaseMetadata.  # noqa: E501
        :type sequence_id: str
        :param sequence_filename: The sequence_filename of this BaseMetadata.  # noqa: E501
        :type sequence_filename: str
        :param isolate_id: The isolate_id of this BaseMetadata.  # noqa: E501
        :type isolate_id: str
        :param institution: The institution of this BaseMetadata.  # noqa: E501
        :type institution: Organization
        :param project_number: The project_number of this BaseMetadata.  # noqa: E501
        :type project_number: str
        :param project_title: The project_title of this BaseMetadata.  # noqa: E501
        :type project_title: str
        :param sampling_date: The sampling_date of this BaseMetadata.  # noqa: E501
        :type sampling_date: datetime
        :param received_date: The received_date of this BaseMetadata.  # noqa: E501
        :type received_date: datetime
        :param sofi_date: The sofi_date of this BaseMetadata.  # noqa: E501
        :type sofi_date: datetime
        :param run_id: The run_id of this BaseMetadata.  # noqa: E501
        :type run_id: str
        :param public: The public of this BaseMetadata.  # noqa: E501
        :type public: str
        :param primary_isolate: The primary_isolate of this BaseMetadata.  # noqa: E501
        :type primary_isolate: bool
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

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BaseMetadata of this BaseMetadata.  # noqa: E501
        :rtype: BaseMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sequence_id(self):
        """Gets the sequence_id of this BaseMetadata.


        :return: The sequence_id of this BaseMetadata.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this BaseMetadata.


        :param sequence_id: The sequence_id of this BaseMetadata.
        :type sequence_id: str
        """
        if sequence_id is None:
            raise ValueError("Invalid value for `sequence_id`, must not be `None`")  # noqa: E501

        self._sequence_id = sequence_id

    @property
    def sequence_filename(self):
        """Gets the sequence_filename of this BaseMetadata.


        :return: The sequence_filename of this BaseMetadata.
        :rtype: str
        """
        return self._sequence_filename

    @sequence_filename.setter
    def sequence_filename(self, sequence_filename):
        """Sets the sequence_filename of this BaseMetadata.


        :param sequence_filename: The sequence_filename of this BaseMetadata.
        :type sequence_filename: str
        """

        self._sequence_filename = sequence_filename

    @property
    def isolate_id(self):
        """Gets the isolate_id of this BaseMetadata.


        :return: The isolate_id of this BaseMetadata.
        :rtype: str
        """
        return self._isolate_id

    @isolate_id.setter
    def isolate_id(self, isolate_id):
        """Sets the isolate_id of this BaseMetadata.


        :param isolate_id: The isolate_id of this BaseMetadata.
        :type isolate_id: str
        """
        if isolate_id is None:
            raise ValueError("Invalid value for `isolate_id`, must not be `None`")  # noqa: E501

        self._isolate_id = isolate_id

    @property
    def institution(self):
        """Gets the institution of this BaseMetadata.


        :return: The institution of this BaseMetadata.
        :rtype: Organization
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this BaseMetadata.


        :param institution: The institution of this BaseMetadata.
        :type institution: Organization
        """
        if institution is None:
            raise ValueError("Invalid value for `institution`, must not be `None`")  # noqa: E501

        self._institution = institution

    @property
    def project_number(self):
        """Gets the project_number of this BaseMetadata.


        :return: The project_number of this BaseMetadata.
        :rtype: str
        """
        return self._project_number

    @project_number.setter
    def project_number(self, project_number):
        """Sets the project_number of this BaseMetadata.


        :param project_number: The project_number of this BaseMetadata.
        :type project_number: str
        """

        self._project_number = project_number

    @property
    def project_title(self):
        """Gets the project_title of this BaseMetadata.


        :return: The project_title of this BaseMetadata.
        :rtype: str
        """
        return self._project_title

    @project_title.setter
    def project_title(self, project_title):
        """Sets the project_title of this BaseMetadata.


        :param project_title: The project_title of this BaseMetadata.
        :type project_title: str
        """

        self._project_title = project_title

    @property
    def sampling_date(self):
        """Gets the sampling_date of this BaseMetadata.


        :return: The sampling_date of this BaseMetadata.
        :rtype: datetime
        """
        return self._sampling_date

    @sampling_date.setter
    def sampling_date(self, sampling_date):
        """Sets the sampling_date of this BaseMetadata.


        :param sampling_date: The sampling_date of this BaseMetadata.
        :type sampling_date: datetime
        """

        self._sampling_date = sampling_date

    @property
    def received_date(self):
        """Gets the received_date of this BaseMetadata.


        :return: The received_date of this BaseMetadata.
        :rtype: datetime
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this BaseMetadata.


        :param received_date: The received_date of this BaseMetadata.
        :type received_date: datetime
        """
        if received_date is None:
            raise ValueError("Invalid value for `received_date`, must not be `None`")  # noqa: E501

        self._received_date = received_date

    @property
    def sofi_date(self):
        """Gets the sofi_date of this BaseMetadata.


        :return: The sofi_date of this BaseMetadata.
        :rtype: datetime
        """
        return self._sofi_date

    @sofi_date.setter
    def sofi_date(self, sofi_date):
        """Sets the sofi_date of this BaseMetadata.


        :param sofi_date: The sofi_date of this BaseMetadata.
        :type sofi_date: datetime
        """

        self._sofi_date = sofi_date

    @property
    def run_id(self):
        """Gets the run_id of this BaseMetadata.


        :return: The run_id of this BaseMetadata.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this BaseMetadata.


        :param run_id: The run_id of this BaseMetadata.
        :type run_id: str
        """
        if run_id is None:
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def public(self):
        """Gets the public of this BaseMetadata.


        :return: The public of this BaseMetadata.
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BaseMetadata.


        :param public: The public of this BaseMetadata.
        :type public: str
        """

        self._public = public

    @property
    def primary_isolate(self):
        """Gets the primary_isolate of this BaseMetadata.


        :return: The primary_isolate of this BaseMetadata.
        :rtype: bool
        """
        return self._primary_isolate

    @primary_isolate.setter
    def primary_isolate(self, primary_isolate):
        """Sets the primary_isolate of this BaseMetadata.


        :param primary_isolate: The primary_isolate of this BaseMetadata.
        :type primary_isolate: bool
        """
        if primary_isolate is None:
            raise ValueError("Invalid value for `primary_isolate`, must not be `None`")  # noqa: E501

        self._primary_isolate = primary_isolate
