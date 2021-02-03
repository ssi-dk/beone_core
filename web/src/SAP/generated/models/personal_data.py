# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .. import util


class PersonalData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """PersonalData - a model defined in OpenAPI

        :param data: The data of this PersonalData.  # noqa: E501
        :type data: str
        """
        self.openapi_types = {
            'data': str
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'PersonalData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PersonalData of this PersonalData.  # noqa: E501
        :rtype: PersonalData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this PersonalData.


        :return: The data of this PersonalData.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PersonalData.


        :param data: The data of this PersonalData.
        :type data: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
