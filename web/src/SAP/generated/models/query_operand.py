# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated.models.query_operator import QueryOperator
from web.src.SAP.generated.models.query_range_inclusivity import QueryRangeInclusivity
from web.src.SAP.generated import util

from web.src.SAP.generated.models.query_operator import QueryOperator  # noqa: E501
from web.src.SAP.generated.models.query_range_inclusivity import QueryRangeInclusivity  # noqa: E501

class QueryOperand(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, operator=None, left=None, right=None, field=None, term=None, inclusive=None, term_min=None, term_max=None, prefix=None):  # noqa: E501
        """QueryOperand - a model defined in OpenAPI

        :param operator: The operator of this QueryOperand.  # noqa: E501
        :type operator: QueryOperator
        :param left: The left of this QueryOperand.  # noqa: E501
        :type left: object
        :param right: The right of this QueryOperand.  # noqa: E501
        :type right: object
        :param field: The field of this QueryOperand.  # noqa: E501
        :type field: str
        :param term: The term of this QueryOperand.  # noqa: E501
        :type term: str
        :param inclusive: The inclusive of this QueryOperand.  # noqa: E501
        :type inclusive: QueryRangeInclusivity
        :param term_min: The term_min of this QueryOperand.  # noqa: E501
        :type term_min: str
        :param term_max: The term_max of this QueryOperand.  # noqa: E501
        :type term_max: str
        :param prefix: The prefix of this QueryOperand.  # noqa: E501
        :type prefix: str
        """
        self.openapi_types = {
            'operator': QueryOperator,
            'left': object,
            'right': object,
            'field': str,
            'term': str,
            'inclusive': QueryRangeInclusivity,
            'term_min': str,
            'term_max': str,
            'prefix': str,
        }

        self.attribute_map = {
            'operator': 'operator',
            'left': 'left',
            'right': 'right',
            'field': 'field',
            'term': 'term',
            'inclusive': 'inclusive',
            'term_min': 'term_min',
            'term_max': 'term_max',
            'prefix': 'prefix',
        }

        self._operator = operator
        self._left = left
        self._right = right
        self._field = field
        self._term = term
        self._inclusive = inclusive
        self._term_min = term_min
        self._term_max = term_max
        self._prefix = prefix

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryOperand of this QueryOperand.  # noqa: E501
        :rtype: QueryOperand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operator(self):
        """Gets the operator of this QueryOperand.


        :return: The operator of this QueryOperand.
        :rtype: QueryOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QueryOperand.


        :param operator: The operator of this QueryOperand.
        :type operator: QueryOperator
        """

        self._operator = operator

    @property
    def left(self):
        """Gets the left of this QueryOperand.


        :return: The left of this QueryOperand.
        :rtype: object
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this QueryOperand.


        :param left: The left of this QueryOperand.
        :type left: object
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this QueryOperand.


        :return: The right of this QueryOperand.
        :rtype: object
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this QueryOperand.


        :param right: The right of this QueryOperand.
        :type right: object
        """

        self._right = right

    @property
    def field(self):
        """Gets the field of this QueryOperand.


        :return: The field of this QueryOperand.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this QueryOperand.


        :param field: The field of this QueryOperand.
        :type field: str
        """

        self._field = field

    @property
    def term(self):
        """Gets the term of this QueryOperand.


        :return: The term of this QueryOperand.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this QueryOperand.


        :param term: The term of this QueryOperand.
        :type term: str
        """

        self._term = term

    @property
    def inclusive(self):
        """Gets the inclusive of this QueryOperand.


        :return: The inclusive of this QueryOperand.
        :rtype: QueryRangeInclusivity
        """
        return self._inclusive

    @inclusive.setter
    def inclusive(self, inclusive):
        """Sets the inclusive of this QueryOperand.


        :param inclusive: The inclusive of this QueryOperand.
        :type inclusive: QueryRangeInclusivity
        """

        self._inclusive = inclusive

    @property
    def term_min(self):
        """Gets the term_min of this QueryOperand.


        :return: The term_min of this QueryOperand.
        :rtype: str
        """
        return self._term_min

    @term_min.setter
    def term_min(self, term_min):
        """Sets the term_min of this QueryOperand.


        :param term_min: The term_min of this QueryOperand.
        :type term_min: str
        """

        self._term_min = term_min

    @property
    def term_max(self):
        """Gets the term_max of this QueryOperand.


        :return: The term_max of this QueryOperand.
        :rtype: str
        """
        return self._term_max

    @term_max.setter
    def term_max(self, term_max):
        """Sets the term_max of this QueryOperand.


        :param term_max: The term_max of this QueryOperand.
        :type term_max: str
        """

        self._term_max = term_max

    @property
    def prefix(self):
        """Gets the prefix of this QueryOperand.


        :return: The prefix of this QueryOperand.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this QueryOperand.


        :param prefix: The prefix of this QueryOperand.
        :type prefix: str
        """

        self._prefix = prefix
