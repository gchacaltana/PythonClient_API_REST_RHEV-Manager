# -*- coding: utf-8 -*-
""" El RhevManager se conecta al API REST del RHEV-Manager"""
 
__author__      = "Gonzalo Chacaltana @gchacaltanab"
 
import requests
import json
from requests.auth import HTTPBasicAuth
 
class RhevManager(object):
 
    def __init__(self,api_url=None,username=None,password=None,cert=None):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.cert = cert
 
    def request(self, url, data = None, method = "GET"):
        headers = self.build_header()
 
        if method == "GET":
            response = requests.get(url,verify=self.cert,auth=HTTPBasicAuth(self.username, self.password),headers=headers)
        if method == "POST":
            pass
 
        if response.status_code == 200 :
            return response.json()
 
        if response.status_code == 201 :
            pass
 
        code_error = "(%s)" % response.status_code
        message = {code_error:response.reason}
 
        if response.status_code == 400 :
            print response.raise_for_status()
 
        if response.status_code == 401 :
            return json.dumps(message)
 
        if response.status_code == 402 :
            return json.dumps(message)
 
        if response.status_code == 403 :
            return json.dumps(message)
 
        if response.status_code == 404 :
            return json.dumps(message)
 
        if response.status_code == 408 :
            return json.dumps(message)
 
        if response.status_code == 500 :
            return json.dumps(message)
 
 
    def get_home_document(self):
        return self.request(self.api_url)
 
    def build_header(self, accept=None, content_type=None):
        accept = "application/json" if accept==None else accept
        content_type = "application/json" if content_type==None else content_type
        return {"Accept":accept, "Content-Type":content_type}
