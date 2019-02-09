# encoding=utf-8
import os

# 获取当前文件所在目录的绝对路径
# parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath('.')))
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放页面的元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath + u"\\config\\PageElementLocator.ini"

# 获取存放页面元素定位表达式文件的绝对路径
dataFilePath = parentDirPath + u"\\testData\\126邮箱联系人.xlsx"

# 126账号工作表中，每列对应的数字序号
account_username = 2
account_password = 3
account_dataBook = 4

