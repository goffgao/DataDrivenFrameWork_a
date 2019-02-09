# encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemsSection("126mail_login")
        print(self.loginOptions)

    def switchToFrame(self):
        try:
            # 从定位表达式配置文件中读取frame的定位表达式
            locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            print(type(locatorExpression),locatorExpression)
            # 由于数据类型是str
            self.driver.switch_to.frame(int(locatorExpression))
            # self.driver.switch_to.frame(0)
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中读取username的定位表达式
            locateType,locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            print(locateType,locatorExpression)
            # 获取登陆页面的用户名输入框页面对象,并返回给调用者
            elementObj = getElement(self.driver, locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise print("元素不存在或加载失败,请增加等待时间验证 %s" % e)

    def passwordObj(self):
        try:
            # 从定位表达式配置文件中读取password的定位表达式
            locateType,locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            print(locateType,locatorExpression)
            # 获取登陆页面的用户名输入框页面对象,并返回给调用者
            elementObj = getElement(self.driver, locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise print("元素不存在或加载失败,请增加等待时间验证 %s" % e)

    def LoginButton(self):
        try:
            # 从定位表达式配置文件中读取登陆loginbutton的定位表达式
            locateType,locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            print(locateType,locatorExpression)
            # 获取登陆页面的用户名输入框页面对象,并返回给调用者
            elementObj = getElement(self.driver, locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise print("元素不存在或加载失败,请增加等待时间验证 %s" % e)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com/")
    import time
    time.sleep(5)
    login = LoginPage(driver)
    login.switchToFrame()
    # 输入登陆用户名
    login.userNameObj().send_keys("goffgao1")
    # 输入登陆密码
    login.passwordObj().send_keys("123456Qw")
    time.sleep(3)
    login.LoginButton().click()
    time.sleep(10)
    login.switchToDefaultFrame()
    assert u"未读邮件" in driver.page_source
    driver.quit()

