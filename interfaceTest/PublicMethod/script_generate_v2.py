import csv
import re
import json
from interfaceTest.Integrate_request.BaseUtil import Util
from interfaceTest.PublicMethod.csv_operation import OperationCSV


class Swagger2:
    def __init__(self, method, url, api_file):
        """

        :param method: 请求方式
        :param url: swagger接口地址 ip/version/api-docs
        :param api_file: path+file_name.csv
        """
        self.filepath = api_file
        self.res = Util().main(method, url).json()
        self.pattern = re.compile(r'parameters')
        self.ref = re.compile('\'\$ref(.*?})')

    def get_api(self):
        value_list = []
        for api_url in self.res['paths']:
            for api_method in self.res['paths'][api_url]:
                if self.pattern.search(str(self.res['paths'][api_url])) is not None:
                    put_url = api_url
                    put_method = api_method
                    value_info = self.res['paths'][api_url][api_method]
                    content_type = value_info['produces']
                    parameters = value_info['parameters']
                    tags = value_info['tags'][0]

                    request_body = parameters[0]['schema']
                    if self.ref.search(str(request_body)) is None:
                        pass
                    else:
                        result = '{' + self.ref.search(str(request_body)).group(0)
                        parameter = json.loads(result.replace("'", '"'))['$ref'] \
                            .replace('#/definitions/', '')                        # print(parameter)
                        value_list.append((put_url, put_method, content_type, parameter, tags))
                        document = OperationCSV(self.filepath)
                        document.write_value(value_list)

    def get_parameter(self, parameter_path):
        """

        :param parameter_path: 参数文件存放路径
        :return:
        """
        with open(self.filepath, 'r') as file:
            reader = csv.reader(file)
            x = []
            for row in reader:
                result = self.res['definitions'][row[3]]['properties']
                x.append((row[3], result))
            for i in x:     # 遍历生成的api.csv,并生成入参文档
                v = []
                value_l = [i[1], 'expected_results', 'assert_method', 'actual_results', 'header']    # OperationCSV.write_value参数格式
                v.append(value_l)
                document = OperationCSV(parameter_path + '/' + i[0] + '.csv')
                document.write_value(v)


"""
    Swagger2('get', 'http://ip/v2/api-docs', '/home/bugpz/文档/api.csv').get_api()
    Swagger2('get', 'http://ip/v2/api-docs', '/home/bugpz/文档/api.csv')\
    .get_parameter('/home/bugpz/文档/test')
"""