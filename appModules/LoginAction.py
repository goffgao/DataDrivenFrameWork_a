# encoding=utf-8
from pageObjects.LoginPage import LoginPage


class LoginAction(object):
    def __init__(self):
        print("Login...")

    @staticmethod
    def login(driver, username, password):
         try:
            login = LoginPage(driver)
            # 将当前焦点切换到登陆模块的frame中,以便能进行后续登录操作
            login.switchToFrame()
            # 输入登陆用户名
            login.userNameObj().send_keys(username)
            # 输入登陆密码
            login.passwordObj().send_keys(password)
            # 点击登陆按钮
            login.LoginButton().click()
            # 切回到默认窗体
            login.switchToDefaultFrame()
         except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    import time
    # 启动Chrome浏览器
    driver = webdriver.Chrome()
    # 访问126邮箱首页
    driver.get("http://mail.126.com")
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(3)
    # 登陆126邮箱
    LoginAction.login(driver,username="goffgao1",password ="123456Qw")
    time.sleep(5)
    driver.quit()
