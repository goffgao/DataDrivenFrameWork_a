# encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class AddressBookPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.addContactsOptions = self.parseCF.getItemsSection("126mail_addContactsPage")
        print(self.addContactsOptions)

    def createContactPersonButton(self):
        # 获取新建联系人按钮
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.createContactsBtn".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonName(self):
        # 获取新建联系人按钮
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.contactPersonName".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.contactPersonEmail".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContacts(self):
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.starContacts".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonMobile(self):
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.contactPersonMobile".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonComment(self):
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.contactPersonComment".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def saveContactPerson(self):
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.savecontacePerson".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
