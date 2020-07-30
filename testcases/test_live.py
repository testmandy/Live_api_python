# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 19:45
# @Author  : mandy
import json

import pytest

from common.Init import TestInit
from common.request import Request
from util.read_ini import ReadIni


class TestLive(TestInit):
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
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    # @pytest.mark.skip
    def test_queryCourseList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryCourseList_uri
        data = {"user_id": 1}
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    # @pytest.mark.skip
    def test_queryList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryList_uri
        data = {
            "tutor_id": 3194,
            "name": "学员",
            "mobile": 13476345567,
            "tag_id": [20, 21],
            "tag_count": 2,
            "currPage": 1,
            "pageSize": 1
        }
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    # @pytest.mark.skip
    def test_getSudentByName(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getSudentByName_uri
        data = {
            "nice_student.tutor_id": 995,
            "nice_student.real_name": "测试",
            "page.currPage": 1,
            "page.pageSize": 10
        }
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    def test_awardCoin(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.awardCoin_uri
        data = [{
            "tutor_id": "4839",
            "coin": 1,
            "users": [cls.users]
        }]
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    # @pytest.mark.skip
    def test_queryStudentAnalysis(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryStudentAnalysis_uri
        data = {
            "course_period_id": "1",
            "lesson_id": "1",
            "teacher_id": "1",
            "class_id": "1"
        }
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)

    # @pytest.mark.skip
    def test_queryStudentList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryStudentList_uri
        data = {
            "course_period_id": "1",
            "lesson_id": "1",
            "teacher_id": "1",
            "class_id": "1"
        }
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u"请求结果为：%s" % res)
        cls.compare_msg(res)
