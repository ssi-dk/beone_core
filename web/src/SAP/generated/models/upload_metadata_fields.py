# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated import util


class UploadMetadataFields(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, sample_id=None, provided_species=None, group=None, experiment_name=None, sequence_run_date=None, sofi_sequence_id=None, project_no=None, project_title=None):  # noqa: E501
        """UploadMetadataFields - a model defined in OpenAPI

        :param sample_id: The sample_id of this UploadMetadataFields.  # noqa: E501
        :type sample_id: str
        :param provided_species: The provided_species of this UploadMetadataFields.  # noqa: E501
        :type provided_species: str
        :param group: The group of this UploadMetadataFields.  # noqa: E501
        :type group: str
        :param experiment_name: The experiment_name of this UploadMetadataFields.  # noqa: E501
        :type experiment_name: str
        :param sequence_run_date: The sequence_run_date of this UploadMetadataFields.  # noqa: E501
        :type sequence_run_date: datetime
        :param sofi_sequence_id: The sofi_sequence_id of this UploadMetadataFields.  # noqa: E501
        :type sofi_sequence_id: str
        :param project_no: The project_no of this UploadMetadataFields.  # noqa: E501
        :type project_no: str
        :param project_title: The project_title of this UploadMetadataFields.  # noqa: E501
        :type project_title: str
        """
        self.openapi_types = {
            'sample_id': str,
            'provided_species': str,
            'group': str,
            'experiment_name': str,
            'sequence_run_date': datetime,
            'sofi_sequence_id': str,
            'project_no': str,
            'project_title': str,
        }

        self.attribute_map = {
            'sample_id': 'sample_id',
            'provided_species': 'provided_species',
            'group': 'group',
            'experiment_name': 'experiment_name',
            'sequence_run_date': 'sequence_run_date',
            'sofi_sequence_id': 'sofi_sequence_id',
            'project_no': 'project_no',
            'project_title': 'project_title',
        }

        self._sample_id = sample_id
        self._provided_species = provided_species
        self._group = group
        self._experiment_name = experiment_name
        self._sequence_run_date = sequence_run_date
        self._sofi_sequence_id = sofi_sequence_id
        self._project_no = project_no
        self._project_title = project_title

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UploadMetadataFields of this UploadMetadataFields.  # noqa: E501
        :rtype: UploadMetadataFields
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sample_id(self):
        """Gets the sample_id of this UploadMetadataFields.


        :return: The sample_id of this UploadMetadataFields.
        :rtype: str
        """
        return self._sample_id

    @sample_id.setter
    def sample_id(self, sample_id):
        """Sets the sample_id of this UploadMetadataFields.


        :param sample_id: The sample_id of this UploadMetadataFields.
        :type sample_id: str
        """

        self._sample_id = sample_id

    @property
    def provided_species(self):
        """Gets the provided_species of this UploadMetadataFields.


        :return: The provided_species of this UploadMetadataFields.
        :rtype: str
        """
        return self._provided_species

    @provided_species.setter
    def provided_species(self, provided_species):
        """Sets the provided_species of this UploadMetadataFields.


        :param provided_species: The provided_species of this UploadMetadataFields.
        :type provided_species: str
        """

        self._provided_species = provided_species

    @property
    def group(self):
        """Gets the group of this UploadMetadataFields.


        :return: The group of this UploadMetadataFields.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UploadMetadataFields.


        :param group: The group of this UploadMetadataFields.
        :type group: str
        """

        self._group = group

    @property
    def experiment_name(self):
        """Gets the experiment_name of this UploadMetadataFields.


        :return: The experiment_name of this UploadMetadataFields.
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this UploadMetadataFields.


        :param experiment_name: The experiment_name of this UploadMetadataFields.
        :type experiment_name: str
        """

        self._experiment_name = experiment_name

    @property
    def sequence_run_date(self):
        """Gets the sequence_run_date of this UploadMetadataFields.


        :return: The sequence_run_date of this UploadMetadataFields.
        :rtype: datetime
        """
        return self._sequence_run_date

    @sequence_run_date.setter
    def sequence_run_date(self, sequence_run_date):
        """Sets the sequence_run_date of this UploadMetadataFields.


        :param sequence_run_date: The sequence_run_date of this UploadMetadataFields.
        :type sequence_run_date: datetime
        """

        self._sequence_run_date = sequence_run_date

    @property
    def sofi_sequence_id(self):
        """Gets the sofi_sequence_id of this UploadMetadataFields.


        :return: The sofi_sequence_id of this UploadMetadataFields.
        :rtype: str
        """
        return self._sofi_sequence_id

    @sofi_sequence_id.setter
    def sofi_sequence_id(self, sofi_sequence_id):
        """Sets the sofi_sequence_id of this UploadMetadataFields.


        :param sofi_sequence_id: The sofi_sequence_id of this UploadMetadataFields.
        :type sofi_sequence_id: str
        """

        self._sofi_sequence_id = sofi_sequence_id

    @property
    def project_no(self):
        """Gets the project_no of this UploadMetadataFields.


        :return: The project_no of this UploadMetadataFields.
        :rtype: str
        """
        return self._project_no

    @project_no.setter
    def project_no(self, project_no):
        """Sets the project_no of this UploadMetadataFields.


        :param project_no: The project_no of this UploadMetadataFields.
        :type project_no: str
        """

        self._project_no = project_no

    @property
    def project_title(self):
        """Gets the project_title of this UploadMetadataFields.


        :return: The project_title of this UploadMetadataFields.
        :rtype: str
        """
        return self._project_title

    @project_title.setter
    def project_title(self, project_title):
        """Sets the project_title of this UploadMetadataFields.


        :param project_title: The project_title of this UploadMetadataFields.
        :type project_title: str
        """

        self._project_title = project_title
