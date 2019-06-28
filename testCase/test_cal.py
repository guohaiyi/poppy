import unittest
from common.cal import Cal


class TestCal(unittest.TestCase):
    def setUp(self) -> None:
        self.cal = Cal()

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.cal.sub(3, 2), 1)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
