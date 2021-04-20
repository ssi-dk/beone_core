# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated import util


class ApprovalAllOf(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, id=None, approver=None, timestamp=None, sequence_ids=None, status=None):  # noqa: E501
        """ApprovalAllOf - a model defined in OpenAPI

        :param id: The id of this ApprovalAllOf.  # noqa: E501
        :type id: str
        :param approver: The approver of this ApprovalAllOf.  # noqa: E501
        :type approver: str
        :param timestamp: The timestamp of this ApprovalAllOf.  # noqa: E501
        :type timestamp: datetime
        :param sequence_ids: The sequence_ids of this ApprovalAllOf.  # noqa: E501
        :type sequence_ids: List[str]
        :param status: The status of this ApprovalAllOf.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'id': str,
            'approver': str,
            'timestamp': datetime,
            'sequence_ids': List[str],
            'status': str,
        }

        self.attribute_map = {
            'id': 'id',
            'approver': 'approver',
            'timestamp': 'timestamp',
            'sequence_ids': 'sequence_ids',
            'status': 'status',
        }

        self._id = id
        self._approver = approver
        self._timestamp = timestamp
        self._sequence_ids = sequence_ids
        self._status = status

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Approval_allOf of this ApprovalAllOf.  # noqa: E501
        :rtype: ApprovalAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ApprovalAllOf.


        :return: The id of this ApprovalAllOf.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApprovalAllOf.


        :param id: The id of this ApprovalAllOf.
        :type id: str
        """

        self._id = id

    @property
    def approver(self):
        """Gets the approver of this ApprovalAllOf.


        :return: The approver of this ApprovalAllOf.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        """Sets the approver of this ApprovalAllOf.


        :param approver: The approver of this ApprovalAllOf.
        :type approver: str
        """

        self._approver = approver

    @property
    def timestamp(self):
        """Gets the timestamp of this ApprovalAllOf.


        :return: The timestamp of this ApprovalAllOf.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ApprovalAllOf.


        :param timestamp: The timestamp of this ApprovalAllOf.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def sequence_ids(self):
        """Gets the sequence_ids of this ApprovalAllOf.


        :return: The sequence_ids of this ApprovalAllOf.
        :rtype: List[str]
        """
        return self._sequence_ids

    @sequence_ids.setter
    def sequence_ids(self, sequence_ids):
        """Sets the sequence_ids of this ApprovalAllOf.


        :param sequence_ids: The sequence_ids of this ApprovalAllOf.
        :type sequence_ids: List[str]
        """

        self._sequence_ids = sequence_ids

    @property
    def status(self):
        """Gets the status of this ApprovalAllOf.


        :return: The status of this ApprovalAllOf.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApprovalAllOf.


        :param status: The status of this ApprovalAllOf.
        :type status: str
        """
        allowed_values = ["pending", "cancelled", "submitted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
