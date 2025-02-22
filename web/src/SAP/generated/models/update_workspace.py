# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated import util


class UpdateWorkspace(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, samples=None):  # noqa: E501
        """UpdateWorkspace - a model defined in OpenAPI

        :param samples: The samples of this UpdateWorkspace.  # noqa: E501
        :type samples: List[str]
        """
        self.openapi_types = {
            'samples': List[str],
        }

        self.attribute_map = {
            'samples': 'samples',
        }

        self._samples = samples

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateWorkspace of this UpdateWorkspace.  # noqa: E501
        :rtype: UpdateWorkspace
        """
        return util.deserialize_model(dikt, cls)

    @property
    def samples(self):
        """Gets the samples of this UpdateWorkspace.


        :return: The samples of this UpdateWorkspace.
        :rtype: List[str]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this UpdateWorkspace.


        :param samples: The samples of this UpdateWorkspace.
        :type samples: List[str]
        """
        if samples is None:
            raise ValueError("Invalid value for `samples`, must not be `None`")  # noqa: E501

        self._samples = samples
