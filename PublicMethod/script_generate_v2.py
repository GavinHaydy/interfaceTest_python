import csv
import re
import json
from Integrate_request.BaseUtil import Util
from PublicMethod.csv_operation import OperationCSV


class Swagger2:
    def __init__(self, method, path, filepath):
        self.filepath = filepath
        self.res = Util().main(method, path).json()
        self.pattern = re.compile(r'parameters')
        self.ref = re.compile('\'\$ref(.*?})')

    def get_api(self):
        value_list = []
        for api_url in self.res['paths']:  # 1
            for api_method in self.res['paths'][api_url]:  # 1
                if self.pattern.search(str(self.res['paths'][api_url])) is not None:
                    put_url = api_url
                    put_method = api_method
                    value_info = self.res['paths'][api_url][api_method]
                    content_type = value_info['produces']
                    parameters = value_info['parameters']

                    request_body = parameters[0]['schema']
                    if self.ref.search(str(request_body)) is None:
                        pass
                    else:
                        result = '{' + self.ref.search(str(request_body)).group(0)
                        parameter = json.loads(result.replace("'", '"'))['$ref'] \
                            .replace('#/definitions/', '')                        # print(parameter)
                        value_list.append((put_url, put_method, content_type, parameter))
                    document = OperationCSV(self.filepath)
                    document.write_value(value_list)

    def get_parameter(self, parameter_path):
        with open(self.filepath, 'r') as file:
            reader = csv.reader(file)
            x = []
            for row in reader:
                result = self.res['definitions'][row[3]]['properties']
                x.append((row[3], result))
            for i in x:     # 遍历生成的api.csv,并生成入参文档
                v = []
                value_l = [i[1], 'assert_method', 'assert_value']    # OperationCSV.write_value参数格式
                v.append(value_l)
                document = OperationCSV(parameter_path + '/' + i[0] + '.csv')
                document.write_value(v)


"""
    from PublicMethod.script_generate import Swagger2

    Swagger2('get', 'http://106.13.171.218/v2/api-docs', '/home/bugpz/文档/api.csv').get_api()
"""

"""
    from PublicMethod.script_generate import Swagger3

Swagger2('get', 'http://106.13.171.218/v2/api-docs', '/home/bugpz/文档/api.csv')\
    .get_parameter('/home/bugpz/文档/test')
"""
