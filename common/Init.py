# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:51
# @Author  : mandy
import pytest

import conftest
from common.request import Request
from util.read_ini import ReadIni


class TestInit(object):
    def setup_class(cls) -> None:
        print(r"--------------------Before Class--------------------")
        cls.readIni = ReadIni()
        cls.base_url = cls.readIni.get_value("base_url")
        cls.schoolweb_url = cls.readIni.get_value("schoolweb_url")
        cls.login_uri = cls.readIni.get_value("padLogin")
        cls.queryCourseList_uri = cls.readIni.get_value("queryCourseList")
        cls.queryList_uri = cls.readIni.get_value("queryList")
        cls.getSudentByName_uri = cls.readIni.get_value("getSudentByName")
        cls.awardCoin_uri = cls.readIni.get_value("awardCoin")
        cls.queryStudentAnalysis_uri = cls.readIni.get_value("queryStudentAnalysis")
        cls.queryStudentList_uri = cls.readIni.get_value("queryStudentList")
        cls.getStudentInfo_uri = cls.readIni.get_value("getStudentInfo")
        cls.getDownLoadUrl_uri = cls.readIni.get_value("getDownLoadUrl")
        cls.qryCourseBanner_uri = cls.readIni.get_value("qryCourseBanner")
        cls.queryGoodsList_uri = cls.readIni.get_value("queryGoodsList")
        cls.queryCourseDetail_uri = cls.readIni.get_value("queryCourseDetail")
        cls.getCourseIsBuy_uri = cls.readIni.get_value("getCourseIsBuy")
        cls.queryRecommendGoods_uri = cls.readIni.get_value("queryRecommendGoods")
        cls.cascadeQuery_uri = cls.readIni.get_value("cascadeQuery")
        cls.studentCourseTask_uri = cls.readIni.get_value("studentCourseTask")
        cls.queryUserAllCourse_uri = cls.readIni.get_value("queryUserAllCourse")
        cls.queryLessonTaskByCourseId_uri = cls.readIni.get_value("queryLessonTaskByCourseId")
        cls.courseCalendar_uri = cls.readIni.get_value("courseCalendar")
        cls.inputSource_uri = cls.readIni.get_value("inputSource")
        cls.table_queryList_uri = cls.readIni.get_value("table_queryList")
        cls.getActivityCouponResource_uri = cls.readIni.get_value("getActivityCouponResource")
        cls.getMyUsableCouponList_uri = cls.readIni.get_value("getMyUsableCouponList")
        cls.getCurrentAndOutdoorQuestions_uri = cls.readIni.get_value("getCurrentAndOutdoorQuestions")

        cls.qryLiveInfo_uri = cls.readIni.get_value("qryLiveInfo", "live")
        cls.getCoin_uri = cls.readIni.get_value("getCoin", "live")
        cls.getSystemMsg_uri = cls.readIni.get_value("getSystemMsg", "live")
        cls.updateRoom_uri = cls.readIni.get_value("updateRoom", "live")
        cls.queryIsCanSpeak_uri = cls.readIni.get_value("queryIsCanSpeak", "live")
        cls.getClearBeforeMsg_uri = cls.readIni.get_value("getClearBeforeMsg", "live")
        cls.onlineNum_uri = cls.readIni.get_value("onlineNum", "live")
        cls.heartBeat_uri = cls.readIni.get_value("heartBeat", "live")

        cls.req = Request()
        cls.headers = {"Content-Type": "application/json;charset=UTF-8",
                   "token": "3552ed08e78b272a2988a1f283ac949cc054"}

    def teardown_class(cls) -> None:
        print(r"--------------------After Class--------------------")
        # cls.op.close()





