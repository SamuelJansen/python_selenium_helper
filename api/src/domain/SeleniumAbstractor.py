from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

###- https://sites.google.com/a/chromium.org/chromedriver/downloads
class SeleniumAbstractor:

    def __init__(self,globals,waittingTime=2):
        self.globals = globals
        self.driverPath = f'{self.globals.apiPath}{self.globals.baseApiPath}resource\\chromedriver.exe'
        self.waittingTime = waittingTime
        self.fractionOfWaittingTime = waittingTime / 7.0
        self.newDriver()

        self.buttomTag = 'button'
        self.aKey = 'a'
        self.closeBraceKey = '}'

    def newDriver(self):
        try :
            self.closeDriver()
        except : pass
        self.driver = webdriver.Chrome(executable_path = self.driverPath)
        self.wait()

    def closeDriver(self):
        self.driver.close()

    def wait(self,fraction=False,processingTime=None):
        if fraction : time.sleep(self.fractionOfWaittingTime)
        elif processingTime : time.sleep(processingTime)
        else : time.sleep(self.waittingTime)

    def getDriver(self,elementRequest):
        if elementRequest : return elementRequest
        else : return self.driver

    def accessUrl(self,url):
        self.driver.get(url)
        self.wait()

    def findButton(self,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_tag_name(self.buttomTag)
        return element

    def accessButton(self,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_tag_name(self.buttomTag)
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
        element = driver.find_element_by_css_selector(f'{self.buttomTag}.{cssClass}')
        return element

    def accessButtonByClass(self,cssClass,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_css_selector(f'{self.buttomTag}.{cssClass}')
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
        return element

    def typeIn(self,text,elementRequest):
        driver = self.getDriver(elementRequest)
        driver.send_keys(Keys.CONTROL, self.aKey)
        driver.send_keys(text)
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
        return driver
