# encoding=utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time

class AddContactPerson(object):
    def __init__(self):
        print("add contact person.")

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            #创建主页实例对象
            hp = HomePage(driver)
            # 单击通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            # 创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                #非必填项
                apb.contactPersonName().send_keys(contactName)
                #必填项
                apb.contactPersonEmail().send_keys(contactEmail)
                if isStar == u"是":
                   # 非必填项
                    apb.starContacts().click()
                if contactPhone:
                    # 非必填
                    apb.contactPersonMobie().send_keys(contactPhone)
                if contactComment:
                    apb.contactPersonComment().send_keys(contactComment)
                apb.saveContactPerson().click()

        except Exception as e:
                # 打印堆栈异常信息
            print(traceback.print_exc())
            raise e

if __name__=='__main__':
    from appModules.LoginAction import LoginAction
    from selenium import webdriver
    import time
    # 启动Chrome浏览器
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    # driver.maximize_window()
    time.sleep(5)
    LoginAction.login(driver,"goffgao1","123456Qw")
    time.sleep(5)
    AddContactPerson.add(driver,u"张三","zs@qq.com",u"是","","")
    time.sleep(3)
    assert u"张三" in driver.page_source
    driver.quit()