#!/usr/bin/python3
# coding=utf-8
from common.operationExcel import OperationExcel
from config.excelConfig import SetExcel
from common.operationJson import OperationJson


class ReadData:
    def __init__(self, file_name=None):
        self.open_excel = OperationExcel()
        self.set_excel = SetExcel()
        if file_name:
            self.open_json = OperationJson(file_name)
        else:
            self.open_json = OperationJson()

    def get_module(self, row):
        cell = self.set_excel.set_method()
        module = self.open_excel.from_cell_get_data(cell, row)
        return module

    def get_api_name(self, row):
        cell = self.set_excel.set_api_name()
        case_id = self.open_excel.from_cell_get_data(cell, row)
        return case_id

    def get_case_id(self, row):
        cell = self.set_excel.set_case_id()
        case_id = self.open_excel.from_cell_get_data(cell, row)
        return case_id

    def get_case_name(self, row):
        cell = self.set_excel.set_case_name()
        case_title = self.open_excel.from_cell_get_data(cell, row)
        return case_title

    def get_url(self, row):
        cell = self.set_excel.set_url()
        url = self.open_excel.from_cell_get_data(cell, row)
        return url

    def get_premise(self, row):
        cell = self.set_excel.set_premise()
        premise = self.open_excel.from_cell_get_data(cell, row)
        return premise

    def get_header(self, row):
        cell = self.set_excel.set_header()
        headers_key = self.open_excel.from_cell_get_data(cell, row)
        headers = self.open_json.key_get_data(headers_key)
        return headers

    def get_method(self, row):
        cell = self.set_excel.set_method()
        method = self.open_excel.from_cell_get_data(cell, row)
        return method

    def get_request_data(self, row):
        cell = self.set_excel.set_data()
        request_key = self.open_excel.from_cell_get_data(cell, row)
        request_data = self.open_json.key_get_data(request_key)
        return request_data

    def get_param(self, row):
        cell = self.set_excel.set_param()
        code = self.open_excel.from_cell_get_data(cell, row)
        return code

    def get_check(self, row):
        cell = self.set_excel.set_check()
        check = self.open_excel.from_cell_get_data(cell, row)
        return check

    def get_expect_result(self, row):
        cell = self.set_excel.set_expected()
        expect_result = self.open_excel.from_cell_get_data(cell, row)
        return expect_result

    def get_return_data(self, row):
        cell = self.set_excel.set_return_data()
        return_data = self.open_excel.from_cell_get_data(cell, row)
        return return_data


if __name__ == "__main__":
    a = ReadData()
    b = a.get_case_name(2)
    print(b)
