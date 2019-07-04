import unittest
from common.cal import Cal
from common.myLog import MyLog


class TestCal(unittest.TestCase):
    def setUp(self) -> None:
        self.cal = Cal()
        self.log = MyLog()

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3), 5, msg='测试不通过，2+3 != 6')
        # self.log.error('测试不通过，2+3 != 6')

    def test_sub(self):
        self.assertEqual(self.cal.sub(3, 2), 2, msg='测试不通过，实际结果：%s' % self.cal.sub(3, 2))

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
