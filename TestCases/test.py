from Integrate_request.BaseUtil import Util
import random
import json
import unittest
from unittest import skip

url = 'http://106.13.171.218'  # 域名
register_api = '/api/user/register'  # 注册接口   post
login_api = '/api/user/login'  # 登录接口 post
allUser = '/api/user'  # 获取所有用户 get
getUserByPhone = '/api/user/'  # 根据手机号查用户 get
updateUser = '/api/user/'  # 修改用户信息    put
delUser = '/api/user/delete/'  # 删除用户  delete
header = {'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                        '537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
phone = random.randint(13000000000, 19999999999)
res = Util()


class Test(unittest.TestCase):
    # 注册
    def test_register_case(self):
        s = res.main('post', url=url+register_api, data=json.dumps(
            {'username': str(phone), 'phone': str(phone), 'sex': '男', 'password': 'e10adc3949ba59abbe56e057f20f883e',
             'email': str(phone) + '@qq.com'}), headers=header)
        self.assertIn('恭喜你注册成功', s.json()['msg'], msg=s.json())
        print(s.json())

