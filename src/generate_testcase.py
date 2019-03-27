import unittest
import HtmlTestRunner
from SeleniumPythonRefactorTestCase import GoogleSearch



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('./report'))