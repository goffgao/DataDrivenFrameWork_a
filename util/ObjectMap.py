# encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    """

    :type locatorExpression: object
    """
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by = locateType, value = locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise print("元素不存在或加载失败,请增加等待时间验证 %s" % e)


if __name__ == '__main__':
    from selenium import webdriver
    # driver = webdriver.Firefox(executable_path= "c:\geckodriver.exe")
    driver = webdriver.Firefox()
    driver.get("https://beta.en.vb.vbio.top/")
    getElement(driver, "id", "login-btn").click()

    # 打印页面对象的标签名
    driver.quit()