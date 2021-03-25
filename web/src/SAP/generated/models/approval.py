# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated.models.approval_all_of import ApprovalAllOf
from web.src.SAP.generated.models.approval_request import ApprovalRequest
from web.src.SAP.generated.models.approval_status import ApprovalStatus
from web.src.SAP.generated import util

from web.src.SAP.generated.models.approval_all_of import ApprovalAllOf  # noqa: E501
from web.src.SAP.generated.models.approval_request import ApprovalRequest  # noqa: E501
from web.src.SAP.generated.models.approval_status import ApprovalStatus  # noqa: E501

class Approval(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, matrix=None, id=None, approver=None, timestamp=None, status=None):  # noqa: E501
        """Approval - a model defined in OpenAPI

        :param matrix: The matrix of this Approval.  # noqa: E501
        :type matrix: Dict[str, Dict[str, ApprovalStatus]]
        :param id: The id of this Approval.  # noqa: E501
        :type id: str
        :param approver: The approver of this Approval.  # noqa: E501
        :type approver: str
        :param timestamp: The timestamp of this Approval.  # noqa: E501
        :type timestamp: datetime
        :param status: The status of this Approval.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'matrix': Dict[str, Dict[str, ApprovalStatus]],
            'id': str,
            'approver': str,
            'timestamp': datetime,
            'status': str,
        }

        self.attribute_map = {
            'matrix': 'matrix',
            'id': 'id',
            'approver': 'approver',
            'timestamp': 'timestamp',
            'status': 'status',
        }

        self._matrix = matrix
        self._id = id
        self._approver = approver
        self._timestamp = timestamp
        self._status = status

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Approval of this Approval.  # noqa: E501
        :rtype: Approval
        """
        return util.deserialize_model(dikt, cls)

    @property
    def matrix(self):
        """Gets the matrix of this Approval.


        :return: The matrix of this Approval.
        :rtype: Dict[str, Dict[str, ApprovalStatus]]
        """
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        """Sets the matrix of this Approval.


        :param matrix: The matrix of this Approval.
        :type matrix: Dict[str, Dict[str, ApprovalStatus]]
        """
        if matrix is None:
            raise ValueError("Invalid value for `matrix`, must not be `None`")  # noqa: E501

        self._matrix = matrix

    @property
    def id(self):
        """Gets the id of this Approval.


        :return: The id of this Approval.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Approval.


        :param id: The id of this Approval.
        :type id: str
        """

        self._id = id

    @property
    def approver(self):
        """Gets the approver of this Approval.


        :return: The approver of this Approval.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        """Sets the approver of this Approval.


        :param approver: The approver of this Approval.
        :type approver: str
        """

        self._approver = approver

    @property
    def timestamp(self):
        """Gets the timestamp of this Approval.


        :return: The timestamp of this Approval.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Approval.


        :param timestamp: The timestamp of this Approval.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this Approval.


        :return: The status of this Approval.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Approval.


        :param status: The status of this Approval.
        :type status: str
        """
        allowed_values = ["pending", "cancelled", "submitted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
