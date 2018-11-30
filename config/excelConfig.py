# -*- coding: UTF-8 -*-
class SetExcel:
    def __init__(self):
        self.case_id = "A"
        self.is_run = "B"
        self.case_title = "C"
        self.precondition = "D"
        self.header = "E"
        self.method = "F"
        self.data = "G"
        self.expect_result = "H"
        self.actual_result = "I"
        self.return_data = "J"

    def set_case(self):
        return self.case_id

    def set_is_run(self):
        return self.is_run

    def set_case_title(self):
        return self.case_title

    def set_precondition(self):
        return self.precondition

    def set_header(self):
        return self.header

    def set_method(self):
        return self.method

    def set_data(self):
        return self.data

    def set_expect_result(self):
        return self.expect_result

    def set_actual_result(self):
        return self.actual_result

    def set_return_data(self):
        return self.return_data


if __name__ == "__main__":
    s = SetExcel()
    a = s.set_return_data()
    print(a)
