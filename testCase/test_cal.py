import unittest
from common.cal import Cal
from common.myLog import MyLog


class TestCal(unittest.TestCase):
    def setUp(self) -> None:
        self.cal = Cal()
        self.log = MyLog()
        self.data = {
            "status": True,
            "results": [
                {
                    "_id": "5d2464d08de42c162fbfe1e6",
                    "tenant_name": "autotest",
                    "db": "autotest",
                    "info": "autotest",
                    "active_status": True
                },
                {
                    "_id": "5d2464d08de42c162fbfe1e7",
                    "tenant_name": "test_autolive",
                    "db": "test_autolive",
                    "info": "test_autolive",
                    "active_status": True
                }
            ]
        }

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3), 5, msg='测试不通过，2+3 != 6')
        self.assertIn('results', self.data)
        self.assertIn('tenant_name', self.data["results"][0])

    def test_sub(self):
        self.assertEqual(self.cal.sub(3, 2), 1, msg='测试不通过，实际结果：%s' % self.cal.sub(3, 2))

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
