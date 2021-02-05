# coding: utf-8

import unittest

from flask import json
from six import BytesIO

from web.src.SAP.generated.models.base_metadata import BaseMetadata  # noqa: E501
from .test import BaseTestCase


class TestUploadController(BaseTestCase):
    """UploadController integration test stubs"""

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_bulk_metadata(self):
        """Test case for bulk_metadata

        
        """
        headers = { 
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(metadata_tsv='metadata_tsv_example')
        response = self.client.open(
            '/api/upload/bulk_metadata',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_multi_upload(self):
        """Test case for multi_upload

        
        """
        headers = { 
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(metadata_tsv='metadata_tsv_example',
                    files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/upload/multi_upload',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_single_upload(self):
        """Test case for single_upload

        
        """
        headers = { 
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(metadata={},
                    file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/upload/single_upload',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
