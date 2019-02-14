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
            time.sleep(3)

            # 单击通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            # 创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                #非必填项
                apb.contactPersonName().send_keys(contactName)
            if contactEmail:
                #必填项
                apb.contactPersonEmail().send_keys(contactEmail)

            if isStar == u"是":
                # 非必填项
                time.sleep(3)
                apb.starContacts().click()

            if contactPhone:
                # 非必填项
                apb.contactPersonMobile().send_keys(contactPhone)
            if contactComment:
                time.sleep(3)
                print("输入comment")
                apb.contactPersonComment().send_keys(contactComment)
            # 点击保存
            apb.saveContactPerson().click()

        except Exception as e:
                # 打印堆栈异常信息
            print(traceback.print_exc())
            raise e


if __name__ == '__main__':
    from appModules.LoginAction import LoginAction
    from selenium import webdriver
    import time
    # 启动Chrome浏览器
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    # driver.maximize_window()
    time.sleep(5)
    LoginAction.login(driver,"goffgao1","123456Qw")
    time.sleep(15)
    AddContactPerson.add(driver,u"张三","zs@qq.com",u"是","123","内容")
    time.sleep(3)
    assert u"张三" in driver.page_source
    print("完成测试")
    driver.quit()