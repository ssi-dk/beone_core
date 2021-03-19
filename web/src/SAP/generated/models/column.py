# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from web.src.SAP.generated.models.organization import Organization
from .. import util

from web.src.SAP.generated.models.organization import Organization  # noqa: E501

class Column(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, approvable=None, editable=None, pii=None, gdpr=None, organizations=None, field_name=None, approves_with=None):  # noqa: E501
        """Column - a model defined in OpenAPI

        :param approvable: The approvable of this Column.  # noqa: E501
        :type approvable: bool
        :param editable: The editable of this Column.  # noqa: E501
        :type editable: bool
        :param pii: The pii of this Column.  # noqa: E501
        :type pii: bool
        :param gdpr: The gdpr of this Column.  # noqa: E501
        :type gdpr: bool
        :param organizations: The organizations of this Column.  # noqa: E501
        :type organizations: List[Organization]
        :param field_name: The field_name of this Column.  # noqa: E501
        :type field_name: str
        :param approves_with: The approves_with of this Column.  # noqa: E501
        :type approves_with: List[str]
        """
        self.openapi_types = {
            'approvable': bool,
            'editable': bool,
            'pii': bool,
            'gdpr': bool,
            'organizations': List[Organization],
            'field_name': str,
            'approves_with': List[str]
        }

        self.attribute_map = {
            'approvable': 'approvable',
            'editable': 'editable',
            'pii': 'pii',
            'gdpr': 'gdpr',
            'organizations': 'organizations',
            'field_name': 'field_name',
            'approves_with': 'approves_with'
        }

        self._approvable = approvable
        self._editable = editable
        self._pii = pii
        self._gdpr = gdpr
        self._organizations = organizations
        self._field_name = field_name
        self._approves_with = approves_with

    @classmethod
    def from_dict(cls, dikt) -> 'Column':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The column of this Column.  # noqa: E501
        :rtype: Column
        """
        return util.deserialize_model(dikt, cls)

    @property
    def approvable(self):
        """Gets the approvable of this Column.

        True if the column can be approved  # noqa: E501

        :return: The approvable of this Column.
        :rtype: bool
        """
        return self._approvable

    @approvable.setter
    def approvable(self, approvable):
        """Sets the approvable of this Column.

        True if the column can be approved  # noqa: E501

        :param approvable: The approvable of this Column.
        :type approvable: bool
        """

        self._approvable = approvable

    @property
    def editable(self):
        """Gets the editable of this Column.

        True if the column can be edited  # noqa: E501

        :return: The editable of this Column.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this Column.

        True if the column can be edited  # noqa: E501

        :param editable: The editable of this Column.
        :type editable: bool
        """

        self._editable = editable

    @property
    def pii(self):
        """Gets the pii of this Column.

        True if the column should be restricted to viewing only by the institution that owns it  # noqa: E501

        :return: The pii of this Column.
        :rtype: bool
        """
        return self._pii

    @pii.setter
    def pii(self, pii):
        """Sets the pii of this Column.

        True if the column should be restricted to viewing only by the institution that owns it  # noqa: E501

        :param pii: The pii of this Column.
        :type pii: bool
        """

        self._pii = pii

    @property
    def gdpr(self):
        """Gets the gdpr of this Column.

        True if the column should be treated as a 'gdpr' column, subject to more strict auditing/logging  # noqa: E501

        :return: The gdpr of this Column.
        :rtype: bool
        """
        return self._gdpr

    @gdpr.setter
    def gdpr(self, gdpr):
        """Sets the gdpr of this Column.

        True if the column should be treated as a 'gdpr' column, subject to more strict auditing/logging  # noqa: E501

        :param gdpr: The gdpr of this Column.
        :type gdpr: bool
        """

        self._gdpr = gdpr

    @property
    def organizations(self):
        """Gets the organizations of this Column.

        List of organizations/institutions who 'own' or should have unrestricted access to this field  # noqa: E501

        :return: The organizations of this Column.
        :rtype: List[Organization]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this Column.

        List of organizations/institutions who 'own' or should have unrestricted access to this field  # noqa: E501

        :param organizations: The organizations of this Column.
        :type organizations: List[Organization]
        """

        self._organizations = organizations

    @property
    def field_name(self):
        """Gets the field_name of this Column.


        :return: The field_name of this Column.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this Column.


        :param field_name: The field_name of this Column.
        :type field_name: str
        """

        self._field_name = field_name

    @property
    def approves_with(self):
        """Gets the approves_with of this Column.

        List of other columns, if any, that should be sent along when this column gets approved  # noqa: E501

        :return: The approves_with of this Column.
        :rtype: List[str]
        """
        return self._approves_with

    @approves_with.setter
    def approves_with(self, approves_with):
        """Sets the approves_with of this Column.

        List of other columns, if any, that should be sent along when this column gets approved  # noqa: E501

        :param approves_with: The approves_with of this Column.
        :type approves_with: List[str]
        """

        self._approves_with = approves_with
