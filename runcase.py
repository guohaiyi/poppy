# -*- coding: UTF-8 -*-
import time
import os
import sys
import unittest
from common.myLog import MyLog
from config.readConfig import ReadConfig
from common.HTMLTestRunnerNew import HTMLTestRunner
from common.sendEmail import SendEmail

proDir = os.path.split(os.path.realpath(__file__))[0]
case_list_path = os.path.join(proDir, "case_list.txt")
test_case_path = os.path.join(proDir, "testCase")


class RunTest:
    def __init__(self):
        # 导入TestCase目录下的全部测试用例
        # self.discover = unittest.defaultTestLoader.discover(test_case_path, pattern='test*.py')
        self.logger = MyLog()
        self.readconfig = ReadConfig()
        self.send_mail = SendEmail()
        self.is_send = self.readconfig.get_email("is_send")
        # 导入指定测试用例列表文件
        self.case_list_file = case_list_path
        self.case_list_list = []
        # 导入测试报告信息
        self.testers = self.readconfig.get_report("testers")
        self.title = self.readconfig.get_report("title")
        self.description = self.readconfig.get_report("description")

    def get_case_list(self):
        """
        获取需要进行运行的测试用例列表
        :return:
        """
        fb = open(self.case_list_file)
        for i in fb.readlines():
            data = str(i)
            if data != '' and not data.startswith('#'):
                self.case_list_list.append(data.replace('\n', ''))
        fb.close()
        print(self.case_list_list)

    def set_test_suite(self):
        """
        设置添加测试套件
        :return:
        """
        self.get_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list_list:
            case_name = case.split('/')[-1]
            print(case_name + '.py')
            discover = unittest.defaultTestLoader.discover(test_case_path, pattern=case_name + '.py')
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run_test(self):
        """
        执行测试
        :return:
        """
        try:
            test_suite = self.set_test_suite()  # 获取测试套件
            now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))  # 获取当前日期时间
            public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
            filename = public_path + "\\report\\" + now + "report.html"  # 保存的报告路径和名称
            fp = open(filename, 'wb')
            runner = HTMLTestRunner(stream=fp,
                                    tester=self.testers,
                                    title=self.title,
                                    description=self.description
                                    )
            if test_suite is not None:
                runner.run(test_suite)  # 执行指定添加的测试用例套件
                # runner.run(self.discover) # 执行TestCase目录下的全部测试用例
            else:
                self.logger.info("Have no case to test.")
        except Exception as e:
            self.logger.error(str(e))
        finally:
            self.logger.warning("============TEST END============")
            fp.close()
            # 发送电子邮件
            if self.is_send == 'yes':
                self.send_mail.send_email()
            elif self.is_send == 'no':
                self.logger.info("不发送电子邮件！")
            else:
                self.logger.error("发送电子邮件为未知状态，请检查配置！")


if __name__ == "__main__":
    run = RunTest()
    run.run_test()
