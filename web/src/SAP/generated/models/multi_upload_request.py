# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .. import util


class MultiUploadRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, metadata_tsv=None, files=None):  # noqa: E501
        """MultiUploadRequest - a model defined in OpenAPI

        :param metadata_tsv: The metadata_tsv of this MultiUploadRequest.  # noqa: E501
        :type metadata_tsv: file
        :param files: The files of this MultiUploadRequest.  # noqa: E501
        :type files: List[file]
        """
        self.openapi_types = {
            'metadata_tsv': file,
            'files': List[file]
        }

        self.attribute_map = {
            'metadata_tsv': 'metadata_tsv',
            'files': 'files'
        }

        self._metadata_tsv = metadata_tsv
        self._files = files

    @classmethod
    def from_dict(cls, dikt) -> 'MultiUploadRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MultiUploadRequest of this MultiUploadRequest.  # noqa: E501
        :rtype: MultiUploadRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata_tsv(self):
        """Gets the metadata_tsv of this MultiUploadRequest.


        :return: The metadata_tsv of this MultiUploadRequest.
        :rtype: file
        """
        return self._metadata_tsv

    @metadata_tsv.setter
    def metadata_tsv(self, metadata_tsv):
        """Sets the metadata_tsv of this MultiUploadRequest.


        :param metadata_tsv: The metadata_tsv of this MultiUploadRequest.
        :type metadata_tsv: file
        """
        if metadata_tsv is None:
            raise ValueError("Invalid value for `metadata_tsv`, must not be `None`")  # noqa: E501

        self._metadata_tsv = metadata_tsv

    @property
    def files(self):
        """Gets the files of this MultiUploadRequest.


        :return: The files of this MultiUploadRequest.
        :rtype: List[file]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this MultiUploadRequest.


        :param files: The files of this MultiUploadRequest.
        :type files: List[file]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files
