# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from web.src.SAP.generated.models.base_model_ import Model
from web.src.SAP.generated import util


class SingleUploadRequest(Model):



    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, metadata=None, files=None):  # noqa: E501
        """SingleUploadRequest - a model defined in OpenAPI

        :param metadata: The metadata of this SingleUploadRequest.  # noqa: E501
        :type metadata: file
        :param files: The files of this SingleUploadRequest.  # noqa: E501
        :type files: List[file]
        """
        self.openapi_types = {
            'metadata': file,
            'files': List[file],
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'files': 'files',
        }

        self._metadata = metadata
        self._files = files

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SingleUploadRequest of this SingleUploadRequest.  # noqa: E501
        :rtype: SingleUploadRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self):
        """Gets the metadata of this SingleUploadRequest.


        :return: The metadata of this SingleUploadRequest.
        :rtype: file
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SingleUploadRequest.


        :param metadata: The metadata of this SingleUploadRequest.
        :type metadata: file
        """

        self._metadata = metadata

    @property
    def files(self):
        """Gets the files of this SingleUploadRequest.


        :return: The files of this SingleUploadRequest.
        :rtype: List[file]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SingleUploadRequest.


        :param files: The files of this SingleUploadRequest.
        :type files: List[file]
        """

        self._files = files
