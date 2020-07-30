# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 19:45
# @Author  : mandy
import json
from common.Init import TestInit
user_id = 3552
course_id = 180
lesson_id = 1232
course_period_id = 344
class_group_id = 25595194246168576
lesson_group_id = 25594916549689344
class_id = 1315
sysCurrencyId = 114


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

    def test_qryLiveInfo(cls):
        # 拼接请求地址
        url = cls.base_url + cls.qryLiveInfo_uri
        data = {"nice_student_course_lesson_learn.lesson_id": lesson_id,
                "nice_student_course_lesson_learn.course_id": course_id,
                "nice_student_course_lesson_learn.course_period_id": course_period_id,
                "nice_student_course_lesson_learn.user_id": user_id}
        cls.get_result(url, data)

    def test_getCoin(cls):
        # 拼接请求地址
        url = cls.base_url + cls.getCoin_uri
        data = {"nice_user_coin_account.user_id": user_id}
        cls.get_result(url, data)

    def test_getSystemMsg(cls):
        # 拼接请求地址
        url = cls.base_url + cls.getSystemMsg_uri
        data = {"sysCurrencyId": sysCurrencyId, "sysType": "classroom.ppt", "groupId": lesson_group_id}
        cls.get_result(url, data)

    def test_updateRoom(cls):
        # 拼接请求地址
        url = cls.base_url + cls.updateRoom_uri
        data = {"course_id": course_id, "course_period_id": course_period_id, "lesson_id": lesson_id,
                "user_id": user_id, "groupId": class_group_id, "type": "enter"}
        cls.get_result(url, data)

    def test_queryIsCanSpeak(cls):
        # 拼接请求地址
        url = cls.base_url + cls.queryIsCanSpeak_uri
        data = {"nice_user_classroom_status.user_id": user_id, "nice_user_classroom_status.course_lesson_id": lesson_id,
                "nice_user_classroom_status.course_period_id": course_period_id}
        cls.get_result(url, data)

    def test_getClearBeforeMsg(cls):
        # 拼接请求地址
        url = cls.base_url + cls.getClearBeforeMsg_uri
        data = {"sysType": "classroom.point", "sysCurrencyId": sysCurrencyId, "groupId": lesson_group_id}
        cls.get_result(url, data)

    def test_onlineNum(cls):
        # 拼接请求地址
        url = cls.base_url + cls.onlineNum_uri
        data = {"class_id": class_id}
        cls.get_result(url, data)

    def test_heartBeat(cls):
        # 拼接请求地址
        url = cls.base_url + cls.heartBeat_uri
        data = {"course_id": course_id, "course_period_id": course_period_id, "lesson_id": lesson_id, "user_id": user_id,
                "class_id": class_id, "group_id": class_group_id}
        cls.get_result(url, data)
