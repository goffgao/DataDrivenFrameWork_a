# encoding=utf-8
import re
from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath,encoding="utf-8")

    def getItemsSection(self,sectionName):
        # 获取配置文件制定section下的所有option键值对
        # 并以字典类型返回给调用者
        """注意:
        使用 self.cf.items(seationName)此种方法获取到的
        配置文件中的options内容均被转换成小写,
        比如,loginPage.frame 被转换成了 loginpage.frame
        """
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self,sectionName, optionName):
        # 获取制定section下指定 option的值
        value = self.cf.get(sectionName, optionName)
        return value


if __name__ == '__main__':
    pc = ParseConfigFile()
    print(pc.getItemsSection("126mail_login"))
    print(pc.getOptionValue("126mail_login","loginPage.frame"))

    print(pc.getItemsSection("126mail_homePage"))
    print(pc.getOptionValue("126mail_homePage","homePage.addressbook"))

    print(pc.getItemsSection("126mail_addContactsPage"))
    print(pc.getOptionValue("126mail_addContactsPage","addContactsPage.createContactsBtn"))


