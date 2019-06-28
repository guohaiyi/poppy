# -*- coding: UTF-8 -*-
import time
import os
import sys
import unittest
from common.HTMLTestRunnerNew import HTMLTestRunner
from common.sendEmail import SendEmail

test_path = './testCase'
discover = unittest.defaultTestLoader.discover(test_path, pattern='test*.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    print(now)
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(public_path)
    filename = public_path + "\\report\\" + now + "report.html"  # 保存的报告路径和名称
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                             tester="HaiYi",
                             title="测试报告",
                             description="运行结果: "
                             )
    runner.run(discover)
    fp.close()
    # send = SendEmail()
    #     # send.send_email()
