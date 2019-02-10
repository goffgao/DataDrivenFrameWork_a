# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from


from appModules.LoginAction import LoginAction
import time
import unittest


class TestMailLogin(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Chrome()
        # 访问126邮箱首页
        self.driver.get("https://mail.126.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def testMailLogin(self):
        try:
            LoginAction.login(driver, "goffgao1", "123456Qw")
            time.sleep(5)
            assert u'未读邮件' in self.driver.page_source
        except Exception as e:
            raise e
        finally:
            # 退出浏览
            print("OK")


if __name__ == '__main__':
    unittest.main()

    TestMailLogin()
    print(u"登陆126邮箱成功!")

