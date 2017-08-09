#-*- coding:utf-8 -*-

import yaml
import re
import json


class TestLoader(object):
    """Loader the yaml file and get the parameters which test use"""
    def __init__(self, file):
        """@file: file string of config yaml"""
        self.params = yaml.load(file)

    def __get_methods(self):
        self.method = self.params["method"]

    def __get_headers(self):
        """compile the headers"""
        self._headers = self.params["headers"]
        for k, v in self._headers.iteritems():
            if "$$" in v:
                methods_string = re.match(r"$$.*$$", v).split(",")[0]
                params_string_list = methods_string.match(r",.*").split(",")
                self._headers[k] = getattr(methods_string, params_string_list)
            else:
                continue

