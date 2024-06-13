# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated import util


class TreeMethod(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SINGLE = "single"
    COMPLETE = "complete"
    AVERAGE = "average"
    WEIGHTED = "weighted"
    CENTROID = "centroid"
    MEDIAN = "median"
    WARD = "ward"
    def __init__(self):  # noqa: E501
        """TreeMethod - a model defined in OpenAPI

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
        :return: The TreeMethod of this TreeMethod.  # noqa: E501
        :rtype: TreeMethod
        """
        return util.deserialize_model(dikt, cls)
