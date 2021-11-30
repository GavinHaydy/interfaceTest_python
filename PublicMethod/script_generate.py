import csv
import re
import json
from Integrate_request.BaseUtil import Util
from PublicMethod.csv_operation import OperationCSV


class Swagger3:
    def __init__(self, method, path, filepath):
        self.filepath = filepath
        self.res = Util().main(method, path).json()
        self.pattern = re.compile(r'requestBody')
        self.pattern1 = re.compile(r'application/json')
        self.ref = re.compile('\'\$ref(.*?})')

    def get_api(self):
        value_list = []
        for api_url in self.res['paths']:
            for api_method in self.res['paths'][api_url]:
                if self.pattern.search(str(self.res['paths'][api_url])) is not None:
                    put_url = api_url
                    put_method = api_method
                    parameter = self.res['paths'][api_url][api_method]['requestBody']['content']
                    for content_type in parameter:
                        request_body = parameter[content_type]['schema']
                        if self.ref.search(str(request_body)) is None:
                            pass
                        else:
                            result = '{' + self.ref.search(str(request_body)).group(0)
                            parameter = json.loads(result.replace("'", '"'))['$ref'] \
                                .replace('#/components/schemas/', '')
                            value_list.append((put_url, put_method, content_type, parameter))
                        document = OperationCSV(self.filepath)
                        document.write_value(value_list)

    def get_parameter(self, parameter_path):
        with open(self.filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                result = self.res['components']['schemas'][row[3]]['properties']
                x = []
                for i in result:
                    x.append((i, result[i]))
                document = OperationCSV(parameter_path + '/' + row[3] + '.csv')
                document.write_value(x)


"""
    from PublicMethod.script_generate import Swagger3

    Swagger3('get', 'http://192.192.192.97:8990/v3/api-docs', '/home/bugpz/文档/api.csv').get_api()
"""

"""
    from PublicMethod.script_generate import Swagger3

Swagger3('get', 'http://192.192.192.97:8990/v3/api-docs', '/home/bugpz/文档/api.csv')\
    .get_parameter('/home/bugpz/文档/ttt')
"""
