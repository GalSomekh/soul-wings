"""
This Module contains AWS helper functions:
manage_kwargs(kwargs, secrets)
    Add AWS creds to kwargs dict
========================================================================================================================
s3_put_file(local_path, bucket, key, secrets, **kwargs)
    Upload file content to provided S3 location
========================================================================================================================
get_s3_url(bucket, key)
    Get S3 url for bucket and key pair
========================================================================================================================
s3_list_objects(bucket, secrets, **kwargs)
    List all keys in a given bucket
========================================================================================================================
s3_delete_key(bucket, key, secrets, **kwargs)
    Delete a given key
"""

import os
import sys

REPO_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_DIRECTORY)

import boto3
from lib.log import getLog


LOG = getLog('AWS')


def manage_kwargs(kwargs,
                  secrets):
    """
    Add AWS creds to kwargs dict

    :param kwargs: (dict)
    :param secrets: (dict) Result from helpers.get_secrets
    :return: (dict) Edited dict
    """

    secrets = secrets or {}

    if not kwargs.get('aws_access_key_id'):
        kwargs['aws_access_key_id'] = secrets.get('aws_access_key_id')

    if not kwargs.get('aws_secret_access_key'):
        kwargs['aws_secret_access_key'] = secrets.get('aws_secret_access_key')

    return kwargs


def s3_put_file(local_path,
                bucket,
                key,
                secrets,
                **kwargs):
    """
    Upload file content to provided S3 location

    :param local_path: (str) path of local file to upload
    :param bucket: (str) bucket name in S3
    :param key: (str) full destination path including file name
    :param secrets: (dict) Result from helpers.get_secrets
    :param kwargs: kwargs for boto3.resource
    """

    kwargs = manage_kwargs(kwargs, secrets)
    resource = boto3.resource('s3', **kwargs)

    resource.meta.client.upload_file(local_path,
                                     bucket,
                                     key,
                                     ExtraArgs={'ACL':'public-read'})

    LOG.info('Put to S3 - %s - %s/%s', local_path, bucket, key)


def get_s3_url(bucket,
               key):
    """
    Get S3 url for bucket and key pair

    :param bucket: (str) bucket name in S3
    :param key: (str) full destination path including file name
    :return: (str) S3 url
    """

    return 'https://%s.s3.amazonaws.com/%s' % (bucket, key)


def s3_list_objects(bucket,
                    secrets,
                    **kwargs):
    """
    List all keys in a given bucket

    :param bucket: (str) bucket name in S3
    :param secrets: (dict) Result from helpers.get_secrets
    :param kwargs: kwargs for boto3.client
    :return: (list of dicts) dict per key
    """

    kwargs = manage_kwargs(kwargs, secrets)
    client = boto3.client('s3', **kwargs)

    res = client.list_objects_v2(Bucket=bucket)

    return res.get('Contents', [])


def s3_delete_key(bucket,
                  key,
                  secrets,
                  **kwargs):
    """
    Delete a given key

    :param bucket: (str) bucket name in S3
    :param key: (str) full destination path including file name
    :param secrets: (dict) Result from helpers.get_secrets
    :param kwargs: kwargs for boto3.client
    """

    kwargs = manage_kwargs(kwargs, secrets)
    resource = boto3.resource('s3', **kwargs)

    resource.Object(bucket, key).delete()

    LOG.info('Deleted from S3 - %s/%s', bucket, key)
