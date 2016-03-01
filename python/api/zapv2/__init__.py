# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2012 ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Client implementation for using the ZAP pentesting proxy remotely.
"""

__docformat__ = 'restructuredtext'

import json
import urllib.request, urllib.parse, urllib.error
from python.api.zapv2.acsrf import acsrf
from python.api.zapv2.ascan import ascan
from python.api.zapv2.ajaxSpider import ajaxSpider
from python.api.zapv2.authentication import authentication
from python.api.zapv2.autoupdate import autoupdate
from python.api.zapv2.brk import brk
from python.api.zapv2.context import context
from python.api.zapv2.core import core
from python.api.zapv2.forcedUser import forcedUser
from python.api.zapv2.httpSessions import httpSessions
from python.api.zapv2.importLogFiles import importLogFiles
from python.api.zapv2.params import params
from python.api.zapv2.pnh import pnh
from python.api.zapv2.pscan import pscan
from python.api.zapv2.reveal import reveal
from python.api.zapv2.script import script
from python.api.zapv2.search import search
from python.api.zapv2.selenium import selenium
from python.api.zapv2.sessionManagement import sessionManagement
from python.api.zapv2.spider import spider
from python.api.zapv2.users import users


class ZapError(Exception):
    """
    Base ZAP exception.
    """
    pass


class ZAPv2(object):
    """
    Client API implementation for integrating with ZAP v2.
    """

    # base JSON api url
    base = 'http://zap/JSON/'
    # base OTHER api url
    base_other = 'http://zap/OTHER/'

    def __init__(self, proxies={'http': 'http://127.0.0.1:8080',
                                'https': 'http://127.0.0.1:8080'}):
        """
        Creates an instance of the ZAP api client.

        :Parameters:
           - `proxies`: dictionary of ZAP proxies to use.

        Note that all of the other classes in this directory are generated
        new ones will need to be manually added to this file
        """
        # self.__proxies = proxies

        self.acsrf = acsrf(self)
        self.ajaxSpider = ajaxSpider(self)
        self.ascan = ascan(self)
        self.authentication = authentication(self)
        self.autoupdate = autoupdate(self)
        self.brk = brk(self)
        self.context = context(self)
        self.core = core(self)
        self.forcedUser = forcedUser(self)
        self.httpsessions = httpSessions(self)
        self.importLogFiles = importLogFiles(self)
        self.params = params(self)
        self.pnh = pnh(self)
        self.pscan = pscan(self)
        self.reveal = reveal(self)
        self.script = script(self)
        self.search = search(self)
        self.selenium = selenium(self)
        self.sessionManagement = sessionManagement(self)
        self.spider = spider(self)
        self.users = users(self)

        self.proxy_handler = urllib.request.ProxyHandler(proxies)
        self.opener = urllib.request.build_opener(self.proxy_handler)
        urllib.request.install_opener(self.opener)

    def _expect_ok(self, json_data):
        """
        Checks that we have an OK response, else raises an exception.

        :Parameters:
           - `json_data`: the json data to look at.
        """
        if type(json_data) == type(list()) and json_data[0] == 'OK':
            return json_data
        raise ZapError(*list(json_data.values()))

    def urlopen(self, *args, **kwargs):
        """
        Opens a url forcing the proxies to be used.

        :Parameters:
           - `args`:  all non-keyword arguments.
           - `kwargs`: all other keyword arguments.
        """
        # kwargs['proxies'] = self.__proxies
        try:
            data = urllib.request.urlopen(*args, **kwargs).read()
            print("INFO FROM {}: {}".format(*args, data))
            if self.isJson(data):
                data = data.decode('utf-8')
                print("INFO FROM {}: {}".format(*args, data))
                return data
            else:
                return data
        except Exception as e:
            print("ARGS: {}".format(*args))
            return ""

    def isJson(self, data):
        try:
            json.loads(data.decode('utf-8'))
            return True
        except Exception as e:
            return False

    def status_code(self, *args, **kwargs):
        """
        Open a url forcing the proxies to be used.

        :Parameters:
           - `args`: all non-keyword arguments.
           - `kwargs`: all other keyword arguments.
        """
        # kwargs['proxies'] = self.__proxies
        return urllib.request.urlopen(*args, **kwargs).getcode()

    def _request(self, url, get):
        """
        Shortcut for a GET request.

        :Parameters:
           - `url`: the url to GET at.
           - `get`: the disctionary to turn into GET variables.
        """
        print("URL == {}".format(url))
        data = self.urlopen("{}{}{}".format(url, '?', str(urllib.parse.urlencode(get))))
        return json.load(data)

    def _request_other(self, url, get):
        """
        Shortcut for an API OTHER GET request.

        :Parameters:
           - `url`: the url to GET at.
           - `get`: the disctionary to turn into GET variables.
        """
        return self.urlopen("{}{}{}".format(url, '?', str(urllib.parse.urlencode(get))))
