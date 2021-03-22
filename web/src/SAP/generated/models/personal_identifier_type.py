# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model

from .. import util

class PersonalIdentifierType(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CPR = "CPR"
    CVR = "CVR"
    CHR = "CHR"
    def __init__(self):  # noqa: E501
        """PersonalIdentifierType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The personal-identifier-type of this PersonalIdentifierType.  # noqa: E501
        :rtype: PersonalIdentifierType
        """
        return util.deserialize_model(dikt, cls)
