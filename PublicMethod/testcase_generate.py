import csv

from PublicMethod.mkdir import mkdir


class CreateCase:
    def __init__(self, url, headers, api_file_path, parameter_folder_path, testcase_files_path, report_type='allure'):
        self.url = url  # API_URL
        self.headers = headers
        self.api_file_path = api_file_path
        self.parameter_folder_path = parameter_folder_path
        self.testcase_files_path = testcase_files_path
        self.report_type = report_type

    def create_case(self):
        with open(self.api_file_path, 'r') as file:     # Api_file
            reader_api = csv.reader(file)
            for i in reader_api:
                api = i[0]
                api_filename = api[1:].replace('/', '_')
                request_method = i[1]
                content_type = i[2]
                body = i[3]
                tag_name = i[4]
                with open(f'{self.parameter_folder_path}/{body}.csv', 'r') as parameter_file:  # 打开DTO(参数文档)
                    reader_body = csv.reader(parameter_file)
                    if self.report_type == 'allure':
                        mkdir(self.testcase_files_path+'/', tag_name)
                        with open(f'{self.testcase_files_path}/{tag_name}/{api_filename}_testcase.py', 'w') as script:  # 创建、编写用例脚本
                            index = 0
                            script.write(f'from Integrate_request.BaseUtil import Util\n'
                                         f'import json\n')
                            for item in reader_body:
                                index = index+1
                                request_body = item[0]
                                expected_results = item[1]
                                assert_method = item[2]
                                actual_results = item[3]
                                header = item[4]
                                if header == 'header':
                                    if actual_results == 'actual_results':
                                        script.write(f'\n\ndef test_{api_filename}_{index}():\n'
                                                     f'\tres = Util(data={request_body}, '
                                                     f'headers={self.headers})\\\n'
                                                     f'\t\t.main("{request_method}", "{self.url}{api}")\n'
                                                     f'\tassert "{expected_results}" in json.dumps(res.json())\n')
                                    else:
                                        script.write(f'\n\ndef test_{api_filename}_{index}():\n'
                                                     f'\tres = Util(data={request_body}, '
                                                     f'headers={self.headers})\\\n'
                                                     f'\t\t.main("{request_method}", "{self.url}{api}")\n'
                                                     f'\tassert "{expected_results}" {assert_method} {actual_results}\n'
                                                     )
                                else:
                                    if actual_results == 'actual_results':
                                        script.write(f'\n\ndef test_{api_filename}_{index}():\n'
                                                     f'\tres = Util(data={request_body}, '
                                                     f'headers={header})\\\n'
                                                     f'\t\t.main("{request_method}", "{self.url}{api}")\n'
                                                     f'\tassert "{expected_results}" in json.dumps(res.json())\n')
                                    else:
                                        script.write(f'\n\ndef test_{api_filename}_{index}():\n'
                                                     f'\tres = Util(data={request_body}, '
                                                     f'headers={header})\\\n'
                                                     f'\t\t.main("{request_method}", "{self.url}{api}")\n'
                                                     f'\tassert "{expected_results}" {assert_method} {actual_results}\n'
                                                     )

                        with open(f'{self.testcase_files_path}/{tag_name}/conftest.py', 'w') as conf:
                            conf.write(f'import os\n'
                                       f'import sys\n'
                                       f"sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"
                                       f" '..')))\n")

    """ 
        if __name__ == '__main__':
         CreateCase('http://106.13.171.218', {"Content-Type": "application/json"}, '/home/bugpz/文档/api_test.csv',
                    '/home/bugpz/文档/test', '/home/bugpz/data/interfaceTest_python/Test').create_case()
    """
