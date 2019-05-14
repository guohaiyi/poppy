# -*- coding: UTF-8 -*-
from common.operationExcel import OperationExcel
from config.excelConfig import SetExcel
from common.operationJson import OperationJson


class ReadData:
    def __init__(self):
        self.open_excel = OperationExcel()
        self.open_json = OperationJson()
        self.set_excel = SetExcel()

    def get_case_id(self, row):
        cell = self.set_excel.set_case_id()
        case_id = self.open_excel.from_cell_get_data(cell, row)
        return case_id

    def get_is_run(self, row):
        cell = self.set_excel.set_is_run()
        is_run = self.open_excel.from_cell_get_data(cell, row)
        return is_run

    def get_case_title(self, row):
        cell = self.set_excel.set_case_title()
        case_title = self.open_excel.from_cell_get_data(cell, row)
        return case_title

    def get_precondition(self, row):
        cell = self.set_excel.set_precondition()
        precondition = self.open_excel.from_cell_get_data(cell, row)
        return precondition

    def get_url(self, row):
        cell = self.set_excel.set_url()
        url = self.open_excel.from_cell_get_data(cell, row)
        return url

    def get_headers(self, row):
        cell = self.set_excel.set_header()
        headers_key = self.open_excel.from_cell_get_data(cell, row)
        headers = self.open_json.key_get_data(headers_key)
        return headers

    def get_method(self, row):
        cell = self.set_excel.set_method()
        method = self.open_excel.from_cell_get_data(cell, row)
        return method

    def get_request_data(self, row):
        cell = self.set_excel.set_request_data()
        request_key = self.open_excel.from_cell_get_data(cell, row)
        request_data = self.open_json.key_get_data(request_key)
        return request_data

    def get_expect_result(self, row):
        cell = self.set_excel.set_expect_result()
        expect_result = self.open_excel.from_cell_get_data(cell, row)
        return expect_result

    def get_actual_result(self, row):
        cell = self.set_excel.set_actual_result()
        actual_result = self.open_excel.from_cell_get_data(cell, row)
        return actual_result

    def get_return_data(self, row):
        cell = self.set_excel.set_return_data()
        return_data = self.open_excel.from_cell_get_data(cell, row)
        return return_data


if __name__ == "__main__":
    a = ReadData()
    b = a.get_request_data(2)
    print(b)
