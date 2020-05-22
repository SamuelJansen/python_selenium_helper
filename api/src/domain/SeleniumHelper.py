from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

###- https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
###- https://sites.google.com/a/chromium.org/chromedriver/downloads
class SeleniumHelper:

    TAG_BODY = 'body'
    TAG_HEADER = 'header'
    TAG_BUTTON = 'button'
    TAG_IMPUT = 'input'
    TAG_FORM = 'form'
    TAG_PRE = 'pre'

    ATTRIBUTE_HREF = 'href'

    def __init__(self,globals,waittingTime=2):
        self.globals = globals
        self.driverPath = f'{self.globals.apiPath}{self.globals.baseApiPath}{self.globals.RESOURCE_BACK_SLASH}chromedriver.exe'
        self.waittingTime = waittingTime
        self.fractionOfWaittingTime = waittingTime / 7.0

        self.aKey = 'a'
        self.closeBraceKey = '}'

        # self.newDriver()

    def newDriver(self):
        try :
            self.closeDriver()
        except :
            pass
        self.driver = webdriver.Chrome(executable_path=self.driverPath)
        self.wait()
        self.driver.find_element_by_tag_name(self.TAG_BODY)

    def reset(self):
        self.driver.switch_to.default_content();
        self.wait(fraction=True)

    def closeDriver(self):
        self.driver.close()

    def wait(self,fraction=False,processingTime=None):
        if fraction :
            time.sleep(self.fractionOfWaittingTime)
        elif processingTime :
            time.sleep(processingTime)
        else :
            time.sleep(self.waittingTime)

    def getDriver(self,elementRequest):
        if elementRequest :
            return elementRequest
        else :
            return self.driver

    def accessUrl(self,url):
        self.driver.get(url)
        self.wait()
        self.driver.find_element_by_tag_name(self.TAG_BODY)
        return self.driver

    def findButton(self,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_tag_name(self.TAG_BUTTON)
        return element

    def accessButton(self,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_tag_name(self.TAG_BUTTON)
        element = element.click()
        self.wait(fraction=True)
        return element

    def findById(self,id,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_id(id)
        return element

    def findByClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_class_name(cssClass)
        return element

    def accessClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_class_name(cssClass)
        element = element.click()
        self.wait(fraction=True)
        return element

    def getTextByClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_class_name(cssClass)
        return element.text

    def findButtonByClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_css_selector(f'{self.TAG_BUTTON}.{cssClass}')
        return element

    def accessButtonByClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_css_selector(f'{self.TAG_BUTTON}.{cssClass}')
        element = element.click()
        self.wait(fraction=True)
        return element

    def accesHiperLink(self,hiperLink,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_link_text(hiperLink)
        ###- element = driver.find_element_by_partial_link_text(hiperLink)
        element = element.click()
        self.wait(fraction=True)
        return element

    def accessId(self,id,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_id(id)
        element = element.click()
        self.wait(fraction=True)
        return element

    def selectAllByClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_class_name(cssClass)
        element.send_keys(Keys.CONTROL, self.aKey)
        self.wait(fraction=True)
        return element

    def typeIn(self,text,elementRequest):
        driver = self.getDriver(elementRequest)
        driver.send_keys(Keys.CONTROL, self.aKey)
        driver.send_keys(text)
        driver.send_keys(Keys.RETURN)
        self.wait(fraction=True)
        return driver

    def typeInSwagger(self,text,elementRequest):
        filteredText = text.strip()
        driver = self.getDriver(elementRequest)
        driver.send_keys(Keys.CONTROL, self.aKey)
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys(Keys.ARROW_LEFT)
        driver.send_keys(filteredText[0])
        driver.send_keys(Keys.ARROW_LEFT)
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys(Keys.ARROW_RIGHT)
        driver.send_keys(text.strip()[1:])
        driver.send_keys(Keys.DELETE)
        self.wait(fraction=True)
        return driver

    def findByTag(self,tagName,elementRequest):
        driver = self.getDriver(elementRequest)
        return driver.find_element_by_tag_name(tagName)

    def findBySelector(self,selector,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_xpath(selector)
        return element

    def accessSelector(self,selector,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_xpath(selector)
        element = element.click()
        self.wait(fraction=True)
        return element

    def findAllByClass(self,className,elementRequest):
        driver = self.getDriver(elementRequest)
        return driver.find_elements_by_class_name(className)
