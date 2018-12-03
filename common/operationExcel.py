# -*- coding: UTF-8 -*-
import os
from openpyxl import load_workbook
from config.excelConfig import SetExcel

proDir = os.path.split(os.path.realpath(__file__))[0]
excelPath = os.path.join(proDir, "../testDataFile/TestCase.xlsx")

class OperationExcel:
    def __init__(self):
        self.set_excel = SetExcel()
        self.open_excel = load_workbook(excelPath).active   # 打开Excel表格

    # 获取Excel表格的总行数
    def get_lines(self):
        line = self.open_excel.max_row
        return line

    # 通过单元格获取数据，例如：A2
    def from_cell_get_data(self, cell, row):
        """
        :param cell: 所在列A, B, ...
        :param row: 所在行1, 2, ...
        :return: 返回该单元格的数据
        """
        value = self.open_excel[cell + str(row)].value
        return value

    # 通过单元格坐标获取数据，例如：(1, 2)
    def from_coordinate_get_data(self, x, y):
        """
        :param row: 横坐标x
        :param column: 纵坐标y
        :return:返回该坐标(x, y)对应的数据
        """
        value = self.open_excel.cell(x, y).value
        return value

    # 写入数据
    def write_data(self, write_name, row, write_value):
        wb = load_workbook(filename=excelPath)
        ws = wb.active
        ws[write_name + str(row)] = write_value
        wb.save(filename=excelPath)


if __name__ == "__main__":
    s = OperationExcel()
    a = s.write_data("A", 3, "oooooooooooooo")
    print(a)
