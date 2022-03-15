import os
from interfaceTest.PublicMethod.script_generate_v2 import Swagger2
from interfaceTest.PublicMethod.testcase_generate import CreateCase
from interfaceTest.PublicMethod.run_script import Script
from time import sleep


class BeforeRun:
    def __init__(self, url, api, file_name, file_path, testcases_path, headers={"Content-Type": "application/json"},
                 report='a'):
        """

        :param url: url
        :param api: swagger_api  default is /v2/api-docs
        :param file_name: path+file_name.csv 定义生成的api文档
        :param file_path: 参数文件存放路径
        :param testcases_path: 测试用例存放路径
        :param headers: 可选
        :param report: 'a' or 'h'
        """
        Swagger2('get', url + api, file_name).get_api()
        Swagger2('get', url + api, file_name) \
            .get_parameter(file_path)
        if report == 'a' or report == 'h':
            CreateCase(url, headers, file_name, file_path, testcases_path, report).create_case()
        else:
            raise ValueError(f'Parameter {report} must be "a" or "h" ')


class Run:
    def __init__(self, cases_directory, file_name, language, file_name_1=None, report='a', report_dir='Report',
                 report_file_name='', report_title='title', description=''):
        """

        :param cases_directory: 用例路径
        :param file_name: 生成的脚本名.py
        :param file_name_1: pytest最终脚本 unittest不用写
        :param language: 按照环境变量的语言写  python or python3
        :param report: a：allure  h: HtmlTestRunner
        :param report_dir: 测试报告存放路径  allure才需要
        :param report_file_name: HtmlTestRunner测试报告文件名
        :param report_title: HtmlTestRunner测试 报告 标题
        :param description: HtmlTestRunner 测试报告描述
        """
        if report == 'a':
            Script(cases_directory, file_name, file_name_1).pytest_script()
            sleep(3)
            os.system(f'{language} {file_name_1}')
            sleep(3)
            os.system(f'pytest --alluredir={report_dir} {file_name_1}')
            os.system(f'allure generate {report_dir}')
        elif report == 'h':
            Script(cases_directory, file_name, file_name_1).unittest_script(
                report_file_name, report_title, description
            )
            sleep(3)
            os.system(f'{language} {file_name}')
        else:
            raise ValueError(f'Parameter {report} must be "a" or "h" ')
