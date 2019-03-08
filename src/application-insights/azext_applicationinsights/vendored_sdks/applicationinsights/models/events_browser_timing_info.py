# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventsBrowserTimingInfo(Model):
    """The browser timing information.

    :param url_path: The path of the URL
    :type url_path: str
    :param url_host: The host of the URL
    :type url_host: str
    :param name: The name of the page
    :type name: str
    :param url: The url of the page
    :type url: str
    :param total_duration: The total duration of the load
    :type total_duration: long
    :param performance_bucket: The performance bucket of the load
    :type performance_bucket: str
    :param network_duration: The network duration of the load
    :type network_duration: long
    :param send_duration: The send duration of the load
    :type send_duration: long
    :param receive_duration: The receive duration of the load
    :type receive_duration: long
    :param processing_duration: The processing duration of the load
    :type processing_duration: long
    """

    _attribute_map = {
        'url_path': {'key': 'urlPath', 'type': 'str'},
        'url_host': {'key': 'urlHost', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'total_duration': {'key': 'totalDuration', 'type': 'long'},
        'performance_bucket': {'key': 'performanceBucket', 'type': 'str'},
        'network_duration': {'key': 'networkDuration', 'type': 'long'},
        'send_duration': {'key': 'sendDuration', 'type': 'long'},
        'receive_duration': {'key': 'receiveDuration', 'type': 'long'},
        'processing_duration': {'key': 'processingDuration', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(EventsBrowserTimingInfo, self).__init__(**kwargs)
        self.url_path = kwargs.get('url_path', None)
        self.url_host = kwargs.get('url_host', None)
        self.name = kwargs.get('name', None)
        self.url = kwargs.get('url', None)
        self.total_duration = kwargs.get('total_duration', None)
        self.performance_bucket = kwargs.get('performance_bucket', None)
        self.network_duration = kwargs.get('network_duration', None)
        self.send_duration = kwargs.get('send_duration', None)
        self.receive_duration = kwargs.get('receive_duration', None)
        self.processing_duration = kwargs.get('processing_duration', None)
