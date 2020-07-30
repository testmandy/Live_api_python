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
        cls.users = cls.readIni.get_value("users", "data")
        cls.req = Request()
        cls.headers = {"Content-Type": "application/json;charset=UTF-8",
                   "token": "3552ed08e78b272a2988a1f283ac949cc054"}

    def teardown_class(cls) -> None:
        print(r"--------------------After Class--------------------")
        # cls.op.close()





