# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 22:15
# @Author  : mandy
import json

from common.Init import TestInit
from common.request import Request
from util.read_ini import ReadIni


class TestSchool(TestInit):
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

    def test_getStudentInfo(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getStudentInfo_uri
        data = {"nice_user_base.user_Id": "3552"}
        cls.get_result(url, data)

    def test_getDownLoadUrl(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getDownLoadUrl_uri
        data = {"type": "c"}
        cls.get_result(url, data)

    def test_qryCourseBanner(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.qryCourseBanner_uri
        data = {"nice_course_banner.appid": "562"}
        cls.get_result(url, data)

    def test_queryGoodsList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryGoodsList_uri
        data = {"subject": "", "version": "", "grade": "395", "user_id": "3552", "order_name": "暑假"}
        cls.get_result(url, data)

    def test_queryCourseDetail(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryCourseDetail_uri
        data = {"id": 18, "goods_id": 8}
        cls.get_result(url, data)

    def test_getCourseIsBuy(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getCourseIsBuy_uri
        data = {"nice_order.goods_id": 8, "nice_order.user_id": "3552", "nice_course_period_student.course_id": 18}
        cls.get_result(url, data)

    def test_queryRecommendGoods(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryRecommendGoods_uri
        data = {"grade": 395}
        cls.get_result(url, data)

    def test_studentCourseTask(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.studentCourseTask_uri
        data = {"nice_course.user_id": "3552"}
        cls.get_result(url, data)

    def test_queryUserAllCourse(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryUserAllCourse_uri
        data = {"student_id": "3552", "is_close": "", "subject": "", "type": "", "name": ""}
        cls.get_result(url, data)

    def test_queryLessonTaskByCourseId(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryLessonTaskByCourseId_uri
        data = {"nice_student_course_lesson_learn.user_id": 3552, "nice_student_course_lesson_learn.course_id": 127,
                "nice_student_course_lesson_learn.course_period_id": 217}
        cls.get_result(url, data)

    def test_courseCalendar(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.courseCalendar_uri
        data = {"nice_course.user_id": "3552"}
        cls.get_result(url, data)

    def test_inputSource(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.inputSource_uri
        data = {"username": "15200000020", "password": "nice123456"}
        cls.get_result(url, data)

    def test_table_queryList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.table_queryList_uri
        data = {"table_name": "nice_region"}
        cls.get_result(url, data)

    def test_getActivityCouponResource(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getActivityCouponResource_uri
        data = {}
        cls.get_result(url, data)

    def test_getMyUsableCouponList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getMyUsableCouponList_uri
        data = {"user_id": "3552"}
        cls.get_result(url, data)

    def test_getCurrentAndOutdoorQuestions(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getCurrentAndOutdoorQuestions_uri
        data = {"course_lesson_id": "1232", "course_period_id": "344"}
        cls.get_result(url, data)
