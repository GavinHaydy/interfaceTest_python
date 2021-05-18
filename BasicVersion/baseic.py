import requests
import random
import json

# 基础版本不用其他框架
# 公共变量
url = 'http://106.13.171.218'  # 域名
register_api = '/api/user/register'  # 注册接口   post
login_api = '/api/user/login'  # 登录接口 post
allUser = '/api/user'  # 获取所有用户 get
getUserByPhone = '/api/user/'  # 根据手机号查用户 get
updateUser = '/api/user/'  # 修改用户信息    put
delUser = '/api/user/delete/'  # 删除用户  delete
header = {'Content-Type': 'application/json', 'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
phone = random.randint(13000000000, 19999999999)
# 注册一个账号
data = json.dumps({'username': 'dasf', 'phone': str(phone), 'sex': '男', 'password': 'e10adc3949ba59abbe56e057f20f883e',
        'email': str(phone) + '@qq.com'})
register = requests.post(url+register_api, headers=header, data=data)
print(data, register, register.headers, register.content, register.url)

# 登录账号并获取token值
data = json.dumps({'phone': str(phone), 'password': 'e10adc3949ba59abbe56e057f20f883e'})
login = requests.post(url + login_api, headers=header, data=data)
token = login.json()['token']
print(token)

#  根据手机号获取用户信息
find_header = {'Authorization': token}
getuser = requests.get(url + getUserByPhone + str(phone), headers=find_header)
print(getuser.json())

# 获取所有用户信息
getAllUser = requests.get(url + allUser, headers=find_header)
print(getAllUser.json())

# 修改用户信息
data = json.dumps(
    {'phone': str(phone), 'password': 'e10adc3949ba59abbe56e057f20f883e', 'username': '123', 'sex': '男',
     'email': str(phone)+'@dd.com'})
update = requests.put(url + updateUser + str(phone), headers=find_header, data=data)
print(update.json())

# 删除用户
data = json.dumps({'phone': str(phone)})
delete = requests.delete(url+delUser+str(phone), headers=find_header, data=data)
print(delete.json())
