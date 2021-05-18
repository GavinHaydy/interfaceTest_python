"""
整合各种请求方式
"""
import requests
import json


class IntegrateRequest:
    # 请求 request方法
    def get_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.get(url, data, headers).json()
        else:
            res = requests.get(url,  data).json()
        return res

    # post 请求方式
    def post_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.post(url, data, headers).json()
        else:
            res = requests.post(url,  data).json()
        return res

    # delete 请求方式
    def delete_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.delete(url, data, headers).json()
        else:
            res = requests.delete(url,  data).json()
        return res

    # put 请求方式
    def put_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.put(url, data, headers)
        else:
            res = requests.put(url, data)
        return res

    # options 请求方式
    def options_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.options(url, data, headers)
        else:
            res = requests.options(url, data)
        return res

    def main_req(self, method, url, data=None, headers=None):
        if method == "get":
            res = self.get_req(url, data, headers)
        elif method == 'post':
            res = self.post_req(url, data, headers)
        elif method == 'delete':
            res = self.delete_req(url, data, headers)
        elif method == 'put':
            res = self.put_req(url, data, headers)
        elif method == 'options':
            res = self.options_req(url, data, headers)
        else:
            res = "你的请求方式暂未开放，请耐心等待"
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True)


"""
if __name__ == "__main__":
    ir = IntegrateRequest()
    method = 'get'
    url = 'http://127.0.0.1:8000/query_article/'
    data = None
    headers = None
    print(ir.main_req(method, url, data, headers))
"""
