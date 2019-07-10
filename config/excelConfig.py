#!/usr/bin/python3
# coding=utf-8
class SetExcel:
    def __init__(self):
        self.module = "A"
        self.api_name = "B"
        self.case_id = "C"
        self.case_name = "D"
        self.url = "E"
        self.premise = "F"
        self.header = "G"
        self.method = "H"
        self.data = "I"
        self.param = "J"
        self.check = "K"
        self.expected = "L"
        self.return_data = "M"

    def set_module(self):
        return self.module

    def set_api_name(self):
        return self.api_name

    def set_case_id(self):
        return self.case_id

    def set_case_name(self):
        return self.case_name

    def set_url(self):
        return self.url

    def set_premise(self):
        return self.premise

    def set_header(self):
        return self.header

    def set_method(self):
        return self.method

    def set_data(self):
        return self.data

    def set_param(self):
        return self.param

    def set_check(self):
        return self.check

    def set_expected(self):
        return self.expected

    def set_return_data(self):
        return self.return_data


if __name__ == "__main__":
    s = SetExcel()
    a = s.set_expected()
    print(a)
