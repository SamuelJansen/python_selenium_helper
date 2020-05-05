from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

###- https://sites.google.com/a/chromium.org/chromedriver/downloads
class Selenium:

    def __init__(self,pathMannanger,timeSleeping=2):
        self.pathMannanger = pathMannanger
        self.driver = webdriver.Chrome(executable_path = f'{self.pathMannanger.apiPath}{self.pathMannanger.baseApiPath}resource\\chromedriver.exe')
        self.timeSleeping = timeSleeping
        self.wait()

    def wait(self):
        time.sleep(self.timeSleeping)

    def chromeNavigationExample(self) :
        ###- pip install chromedriver
        ###- driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\chromedriver.exe')
        ###- driver = webdriver.Chrome(executable_path = 'C:\\Users\\samuel.jansen\\AppData\\Local\\Programs\\Python\\Python38-32\\chromedriver-Windows')
        self.driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        self.driver.close()

    def getDriver(self,elementRequest):
        if elementRequest : return elementRequest
        else : return self.driver

    def accessUrl(self,url):
        self.driver.get(url)
        self.wait()

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
        element.click()

    def accesHiperLink(self,hiperLink,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_link_text(hiperLink)
        element.click()
        ###- element = driver.find_element_by_partial_link_text(hiperLink)

    def accessId(self,id,elementRequest):
        driver = self.getDriver(elementRequest)
        element = driver.find_element_by_id(id)
        element.click()
