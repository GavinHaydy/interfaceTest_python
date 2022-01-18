import json

import requests

'''
整合各种请求
'''


class Util:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.data = json.dumps(kwargs.get("data", {}))
        self.headers = kwargs.get('headers', {})
        self.params = kwargs.get('params', {})

    def post(self, url):

        return requests.post(url, data=self.data, headers=self.headers)

    def get(self, url):
        return requests.get(url, params=self.params)

    def put(self, url):
        return requests.put(url, data=self.data)

    @staticmethod
    def delete(url):
        return requests.delete(url)

    @staticmethod
    def options(url):
        return requests.options(url)

    def main(self, method, url):
        if method == 'post':
            return self.post(url)
        if method == 'get':
            return self.get(url)
        if method == 'put':
            return self.put(url)
        if method == 'delete':
            return self.delete(url)
        if method == 'options':
            return self.options(url)
