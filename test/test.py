import unittest
import sys
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始================>")
    
    @classmethod
    def tearDownClass(cls):
        print("结束=================>")

    
    def test_0001(self):
        print(sys._getframe().f_code.co_name)

    def test_0002(self):
        print(sys._getframe().f_code.co_name)
    
    def test_0003(self):
        print(sys._getframe().f_code.co_name)

    def test_0004(self):
        print(sys._getframe().f_code.co_name)

    def test_0005(self):
        print(sys._getframe().f_code.co_name)
    
    def test_0006(self):
        print(sys._getframe().f_code.co_name)

    def test_0007_0(self):
        print(sys._getframe().f_code.co_name)

    def test_0007_1(self):
        print(sys._getframe().f_code.co_name)
    
    def test_0007_2(self):
        print(sys._getframe().f_code.co_name)

    def test_0007_3(self):
        print(sys._getframe().f_code.co_name)

    def test_0008(self):
        print(sys._getframe().f_code.co_name)
    
    def test_0009(self):
        print(sys._getframe().f_code.co_name)

    def test_0010(self):
        print(sys._getframe().f_code.co_name)

    def test_0011(self):
        print(sys._getframe().f_code.co_name)
    
    def test_0012(self):
        print(sys._getframe().f_code.co_name)




if __name__ == '__main__':
    unittest.main()
    unittest.main(verbosity=2)   