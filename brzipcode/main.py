# coding: utf-8
import requests
import json

SERVICE_URL = 'http://brzipcode.appspot.com/info?zip_code=%(zip_code)s&token=%(token)s&format=json'

class BRZipCode(object):
    @classmethod
    def get(cls, zip_code, token, plain_text=False):
        req = requests.get(SERVICE_URL % {
            'zip_code': zip_code,
            'token': token,
        })
        
        if plain_text:
            return req.content
        return json.loads(req.content)