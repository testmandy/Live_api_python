# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:22
# @Author  : mandy
import configparser

import conftest


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conftest.env_dir
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding="utf-8")
        return read_ini

    def get_value(self, key, section=None):
        if section is None:
            section = 'api'
        else:
            section = section
        return self.data.get(section, key)


# if __name__ == '__main__':
#     readIni = ReadIni()
#     print(readIni.file_path)
#     local = readIni.get_value("base_url", "api")
#     print(local)
