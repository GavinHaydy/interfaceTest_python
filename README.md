# interfaceTest
  接口自动化测试库

# 注意事项
 需提前下载allure2并配置路径
#requests官方文档   
    https://docs.python-requests.org/zh_CN/latest/
  
 # 目录说明
 ```
.
├─ BasicVersion 
│    └─ baseic.py   # 基础用法
├─ Integrate_request
│    └─ BaseUtil.py  # 整合常用的请求方法
├─ README.md    
├─ Report
│    └─ 存放测试报告的地方
├─ TestCases
│    ├─ __pycache__
│    │    └─ test.cpython-37.pyc
│    └─ test.py # 例子
├─ requirements.txt
└─ run.py # 运行文件
```

 # 使用方法
```python
from interfaceTest.PublicMethod.run_testcase import BeforeRun, Run
BeforeRun('url', 'api', '接口文件.csv', '参数文档存储路径', '用例路径')
Run('用例路径', '脚本1.py', '脚本2.py', 'path里的python名') #RUN 写完参数后运行
```

# 流程图
```mermaid
	graph TB
	A[swagger]---A1[Get_API,Get_parameter]-->B{CreateCase}
	B.-D(allure).->E{create_script type='allure+pytest'}
	B.-F(HTR).->H{create_script type='HtmlTestRunner+unittest'}
	E---R((run_testcase and generate_report </br></br>END</br></br>))
	H---R((run_testcase and generate_report </br></br>END</br></br>))	
	style A fill:#2ff,fill-opacity:0.1,stroke:#faa,stroke-width:4px
	style R stroke:#945,stroke-width:10px
```



