import json

from interfaceTest.Integrate_request.BaseUtil import Util
import re
res = Util()
pattern = re.compile(r'requestBody')
pattern1 = re.compile(r'application/json')
ref = re.compile('\'\$ref(.*?})')

s = res.main('get', 'http://192.192.192.97:8990/v3/api-docs').json()
for i in s['paths']:
    for j in s['paths'][i]:
        if pattern.search(str(s['paths'][i])) is not None:
            url = i
            method = j
            parameter = s['paths'][i][j]['requestBody']['content']
            for x in parameter:
                h = parameter[x]['schema']
            if ref.search(str(h)) is None:
                pass
            else:
                rc = '{' + ref.search(str(h)).group(0)
                parameter = json.loads(rc.replace("'", '"'))['$ref'].replace('#/components/schemas/', '')
            print(url, method, x, parameter)



