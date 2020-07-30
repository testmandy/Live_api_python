# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 22:15
# @Author  : mandy
import json

from common.Init import TestInit
from common.request import Request
from util.read_ini import ReadIni


class TestLive(TestInit):
    def get_result(cls, url, data):
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    def compare_msg(cls, res):
        json_res = json.loads(res)
        if json_res["msg"] == ('success' or 'SUCCESS'):
            print(u"------------测试通过(^_^)------------")
        else:
            print(u"------------测试未通过/(ㄒoㄒ)/~~------------")

    # @pytest.mark.skip
    def test_login_success(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.login_uri
        data = {"username": "15200000020", "password": "nice123456"}
        cls.get_result(url, data)

