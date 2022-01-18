import os
import re


class Script:
    def __init__(self, path, file_name, file_name_1):
        self.path = path
        self.file_name = file_name
        self.file_name_1 = file_name_1
        par = re.compile(r'api_')
        tags = []
        func_name = []
        api_path = []
        for i in os.listdir(f'./{self.path}'):
            tags.append(f'{i}')

        with open(f'./{self.file_name}', 'a') as file_map:
            for tag in tags:
                for func in os.listdir(f'./{self.path}/{tag}'):
                    func = func.replace('.py', '')
                    func_name.append(func)
                    if par.match(func):
                        api_path.append(f'./{self.path}/{tag}/{func}.py')
                        file_map.write(f'from {self.path}.{tag} import {func}\n')
            file_map.write(f'import re\n'
                           f'\n\n'
                           f'par = re.compile(r"test_")\n'
                           f'list_dir = []\n')

            for tag_1 in tags:
                for h in os.listdir(f'./{self.path}/{tag_1}'):
                    h = h.replace('.py', '')
                    if par.match(h):
                        file_map.write(f'{h}_dir = dir({h})\n'
                                       f'for {h}_fun in {h}_dir:\n'
                                       f'\tif {h}_fun != []:\n'
                                       f'\t\tif par.match({h}_fun):\n'
                                       f'\t\t\tlist_dir.append("{h}."+{h}_fun)\n')
            file_map.write(f'\nwith open("./{self.file_name_1}", "a") as file:\n'
                           f'\tfile.write(f"\\n\\n\"\n'
                           f'\t\t\tf"def test():\\n")\n'
                           f'\tfor i in list_dir:\n\t\t'
                           f'file.write(f"\\t{{i}}()\\n")')

        with open(f'./{self.file_name_1}', 'a') as file_testcase:
        
            for j1 in tags:
                for x1 in os.listdir(f'./{self.path}/{j1}'):
                    x1 = x1.replace('.py', '')
                    api_path.append(x1)
                    if par.match(x1):
                        file_testcase.write(f'from {self.path}.{j1} import {x1}\n')


if __name__ == '__main__':
    Script('Test', 'sc.py', 'sc1.py')
