import unittest


class PrintTest(unittest.TestCase):
    def setUp(self):
        self.num = 3
        print("num0:%s" % self.num)

    def test_test1(self):
        self.num = self.num + 3
        print("num1:%s" % (self.num))
        self.assertEqual(self.num, 6, "self.num发生改变不等于3")

    def test_test2(self):
        print("num2:%s" % self.num)

    def tearDown(self):
        self.num = 0
        print("num3:%s" % self.num)


if __name__ == '__main__':
    unittest.main()