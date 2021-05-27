import requests
'''
整合各种请求
'''


class Util:
    @staticmethod
    def post(**kwargs):
        return requests.post(**kwargs)

    @staticmethod
    def get(**kwargs):
        return requests.get(**kwargs)

    @staticmethod
    def put(**kwargs):
        return requests.put(**kwargs)

    @staticmethod
    def delete(**kwargs):
        return requests.delete(**kwargs)

    @staticmethod
    def options(**kwargs):
        return requests.options(**kwargs)

    def main(self, method, **kwargs):
        if method == 'post':
            return self.post(**kwargs)
        if method == 'get':
            return self.get(**kwargs)
        if method == 'put':
            return self.put(**kwargs)
        if method == 'delete':
            return self.delete(**kwargs)
        if method == 'options':
            return self.options(**kwargs)
