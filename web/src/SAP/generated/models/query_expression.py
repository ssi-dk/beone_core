# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model

from .. import util

class QueryExpression(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, left=None, operator=None, right=None):  # noqa: E501
        """QueryExpression - a model defined in OpenAPI

        :param left: The left of this QueryExpression.  # noqa: E501
        :type left: Operand
        :param operator: The operator of this QueryExpression.  # noqa: E501
        :type operator: str
        :param right: The right of this QueryExpression.  # noqa: E501
        :type right: Operand
        """
        self.openapi_types = {
            'left': Operand,
            'operator': str,
            'right': Operand
        }

        self.attribute_map = {
            'left': 'left',
            'operator': 'operator',
            'right': 'right'
        }

        self._left = left
        self._operator = operator
        self._right = right

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The query-expression of this QueryExpression.  # noqa: E501
        :rtype: QueryExpression
        """
        return util.deserialize_model(dikt, cls)

    @property
    def left(self):
        """Gets the left of this QueryExpression.


        :return: The left of this QueryExpression.
        :rtype: Operand
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this QueryExpression.


        :param left: The left of this QueryExpression.
        :type left: Operand
        """

        self._left = left

    @property
    def operator(self):
        """Gets the operator of this QueryExpression.


        :return: The operator of this QueryExpression.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QueryExpression.


        :param operator: The operator of this QueryExpression.
        :type operator: str
        """
        allowed_values = ["AND", "OR", "AND NOT", "OR NOT", "<implicit>"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def right(self):
        """Gets the right of this QueryExpression.


        :return: The right of this QueryExpression.
        :rtype: Operand
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this QueryExpression.


        :param right: The right of this QueryExpression.
        :type right: Operand
        """

        self._right = right
