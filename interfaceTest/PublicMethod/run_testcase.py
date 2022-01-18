import os
from interfaceTest.PublicMethod.script_generate_v2 import Swagger2
from interfaceTest.PublicMethod.testcase_generate import CreateCase
from interfaceTest.PublicMethod.run_script import Script
from time import sleep


class Run:
    def __init__(self, url, api, file_name, file_path, testcases_path, headers={"Content-Type": "application/json"}):
        Swagger2('get', url+api, file_name).get_api()
        Swagger2('get', url+api, file_name)\
            .get_parameter(file_path)
        CreateCase(url, headers, file_name, file_path, testcases_path).create_case()

    @staticmethod
    def run(path, file_name, file_name_1, language):
        Script(path, file_name, file_name_1)
        sleep(3)
        os.system(f'{language} sc.py')
        sleep(3)
        os.system(f'pytest --alluredir=Report {file_name_1}')
        os.system(f'allure generate Report')


# if __name__ == '__main__':
#     Run('http://106.13.171.218', '/v2/api-docs', '/home/bugpz/文档/api_t1.csv', '/home/bugpz/文档/test_1', './Test')\
#         .run('Test', 'sc.py', 'sc1.py', 'python3')
