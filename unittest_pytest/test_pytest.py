import pytest
class TestPrint:
    def setup(self):
        self.num = 3
        print("num0:%s"%self.num)

    def test_test1(self):
        self.num= self.num+3
        print("num1:%s"%(self.num))
        assert self.num==3,"self.num发生改变不等于3"

    def test_test2(self):
        print("num2:%s"%self.num)

    def teardown(self):
        self.num = 0
        print("num3:%s"%self.num)


if __name__ == '__main__':
    pytest.main(['-s', 'test_pytest.py'])