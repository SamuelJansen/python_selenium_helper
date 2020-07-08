from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui, pyperclip
import time, os

###- https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
###- https://sites.google.com/a/chromium.org/chromedriver/downloads
class SeleniumHelper:

    TAG_BODY = 'body'
    TAG_SELECT = 'select'
    TAG_OPTION = 'option'
    TAG_HEADER = 'header'
    TAG_BUTTON = 'button'
    TAG_IMPUT = 'input'
    TAG_TABLE = 'table'
    TAG_FORM = 'form'
    TAG_PRE = 'pre'
    TAG_BR = 'br'

    ATTRIBUTE_HREF = 'href'

    def __init__(self,globals,waittingTime=2):
        self.globals = globals
        self.pyautogui = pyautogui
        self.time = time
        self.pyautogui.FAILSAFE = True
        self.pyperclip = pyperclip
        self.waittingTime = waittingTime
        self.fractionOfWaittingTime = waittingTime / 7.0
        self.driverPath = f'{self.globals.apiPath}api{self.globals.OS_SEPARATOR}resource{self.globals.OS_SEPARATOR}dependency{self.globals.OS_SEPARATOR}chromedriver.exe'
        self.aKey = 'a'
        self.closeBraceKey = '}'

    def newDriver(self):
        try :
            self.closeDriver()
        except Exception as exception :
            self.globals.debug(f'{self.globals.ERROR}Failed to close driver. Cause: {str(exception)}')
        try :
            try :
                self.driver = webdriver.Chrome(ChromeDriverManager().install()) ### webdriver.Chrome(executable_path=self.driverPath)
            except Exception as exception :
                self.globals.debug(f'Failed to load web driver from default library. Going for a second attempt by another library. Cause: {str(exception)}')
                self.driver = webdriver.Chrome(executable_path=self.driverPath)
            self.wait()
            return self.driver.find_element_by_tag_name(self.TAG_BODY)
        except Exception as exception :
            self.globals.debug(f'Failed to creat a new driver. Cause: {str(exception)}')

    def reset(self):
        try :
            self.driver.switch_to.default_content();
            self.wait(fraction=True)
        except Exception as exception :
            self.globals.debug(f'Failed to reset driver. Cause: {str(exception)}')

    def closeDriver(self):
        try :
            self.driver.close()
        except Exception as exception :
            self.globals.debug(f'Failed to close driver. Cause: {str(exception)}')

    def wait(self,fraction=False,processingTime=None):
        if fraction :
            self.time.sleep(self.fractionOfWaittingTime)
        elif processingTime :
            self.time.sleep(processingTime)
        else :
            self.time.sleep(self.waittingTime)

    def copyPasteAutoguiAfterElementClicked(self,text):
        try :
            self.pyperclip.copy(text)
            self.pyautogui.hotkey("ctrl", "v")
            self.wait()
        except Exception as exception :
            self.globals.debug(f'Failed to copy paste text (by pyautogui). Cause: {str(exception)}')

    def paste(self,text,elementRequest):
        try :
            os.system("echo %s| clip" % text.strip())
            elementRequest.send_keys(Keys.CONTROL, 'v')
            self.wait()
        except Exception as exception :
            self.globals.debug(f'Failed to paste text to the element. Cause: {str(exception)}')

    def getDriver(self,elementRequest):
        try :
            self.wait(fraction=True)
            if elementRequest :
                return elementRequest
            else :
                return self.driver
        except Exception as exception :
            self.globals.debug(f'Failed to get driver. Cause: {str(exception)}')

    def accessUrl(self,url,waittingTime=0,acceptAlert=False,ignoreAlert=False):
        try :
            self.driver.get(url)
            self.wait()
            self.wait(processingTime = waittingTime)
            self.handleAlertBox(waittingTime=waittingTime,acceptAlert=acceptAlert,ignoreAlert=ignoreAlert)
            self.driver.find_element_by_tag_name(self.TAG_BODY)
            return self.driver
        except Exception as exception :
            self.globals.debug(f'Failed to access url. Cause: {str(exception)}')

    def refreshPage(self):
        try :
            self.driver.refresh()
            self.wait()
        except Exception as exception :
            print(f'{self.globals.ERROR}Failed to refresh page. Cause: {str(exception)}')

    def handleAlertBox(self,waittingTime=0,acceptAlert=False,ignoreAlert=False):
        resolved = False
        self.wait(processingTime = waittingTime)
        try :
            if ignoreAlert :
                self.driver.switch_to.alert.ignore()
                resolved = True
            elif acceptAlert :
                self.driver.switch_to.alert.accept()
                resolved = True
            return resolved
        except Exception as exception :
            self.globals.debug(f'No alertFound. Cause: {str(exception)}')
            return resolved

    def findButton(self,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_tag_name(self.TAG_BUTTON)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to find button. Cause: {str(exception)}')

    def accessButton(self,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_tag_name(self.TAG_BUTTON)
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access button. Cause: {str(exception)}')

    def findById(self,id,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_id(id)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to find by id. Cause: {str(exception)}')

    def findByClass(self,cssClass,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_class_name(cssClass)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to find by class. Cause: {str(exception)}')

    def accessClass(self,cssClass,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_class_name(cssClass)
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access class. Cause: {str(exception)}')

    def accessTag(self,tagName,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_tag_name(tagName)
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access tag. Cause: {str(exception)}')

    def getTextByClass(self,cssClass,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_class_name(cssClass)
            return element.text
        except Exception as exception :
            self.globals.debug(f'Failed to get text by class. Cause: {str(exception)}')

    def getTextBySelector(self,selector,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_xpath(selector)
            return element.text
        except Exception as exception :
            self.globals.debug(f'Failed to get text by selector. Cause: {str(exception)}')

    def findButtonByClass(self,cssClass,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_css_selector(f'{self.TAG_BUTTON}.{cssClass}')
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to find button by class. Cause: {str(exception)}')

    def accessButtonByClass(self,cssClass,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_css_selector(f'{self.TAG_BUTTON}.{cssClass}')
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access button by class. Cause: {str(exception)}')

    def accesHiperLink(self,hiperLink,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_link_text(hiperLink)
            ###- element = driver.find_element_by_partial_link_text(hiperLink)
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access hyperlink. Cause: {str(exception)}')

    def accessId(self,id,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_id(id)
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access id. Cause: {str(exception)}')

    def selectAllByClass(self,cssClass,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_class_name(cssClass)
            element.send_keys(Keys.CONTROL, self.aKey)
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to select all by class. Cause: {str(exception)}')

    def typeIn(self,text,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            driver.send_keys(Keys.CONTROL, self.aKey)
            driver.send_keys(text)
            self.wait(fraction=True)
            return driver
        except Exception as exception :
            self.globals.debug(f'Failed to type in. Cause: {str(exception)}')

    def typeInAndHitEnter(self,text,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            driver.send_keys(Keys.CONTROL, self.aKey)
            driver.send_keys(text)
            driver.send_keys(Keys.RETURN)
            self.wait(fraction=True)
            return driver
        except Exception as exception :
            self.globals.debug(f'Failed to type in. Cause: {str(exception)}')

    def hitEnter(self,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            driver.send_keys(Keys.RETURN)
            return driver
        except Exception as exception :
            self.globals.debug(f'Failed to hit enter. Cause: {str(exception)}')

    def typeInSwagger(self,text,elementRequest):
        try :
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
        except Exception as exception :
            self.globals.debug(f'Failed to type in swagger. Cause: {str(exception)}')

    def findByTag(self,tagName,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            return driver.find_element_by_tag_name(tagName)
        except Exception as exception :
            self.globals.debug(f'Failed to find by tag. Cause: {str(exception)}')

    def findBySelector(self,selector,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_xpath(selector)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to find by selector. Cause: {str(exception)}')

    def accessSelector(self,selector,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            element = driver.find_element_by_xpath(selector)
            element = element.click()
            self.wait(fraction=True)
            return element
        except Exception as exception :
            self.globals.debug(f'Failed to access selector. Cause: {str(exception)}')

    def findAllByClass(self,className,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            return driver.find_elements_by_class_name(className)
        except Exception as exception :
            self.globals.debug(f'Failed to find all by class. Cause: {str(exception)}')

    def findAllByTag(self,tagName,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            return driver.find_elements_by_tag_name(tagName)
        except Exception as exception :
            self.globals.debug(f'Failed to find all by tag. Cause: {str(exception)}')

    def findAllBySelector(self,selector,elementRequest):
        try :
            driver = self.getDriver(elementRequest)
            return driver.find_elements_by_xpath(selector)
        except Exception as exception :
            self.globals.debug(f'Failed to find all by class. Cause: {str(exception)}')

    def clickElement(self,elementRequest):
        try :
            elementRequest.click()
        except Exception as exception :
            self.globals.debug(f'Failed to click element {str(element)}. Cause: {str(exception)}')

    def calculateAndClick(self,position,fatherSize):
        try :
            windowX = self.driver.execute_script("return window.screenX")
            windowY = self.driver.execute_script("return window.screenY")
            windowOuterWidth = self.driver.execute_script("return window.outerWidth")
            windowOuterHeight = self.driver.execute_script("return window.outerHeight")
            windowInnerWidth = self.driver.execute_script("return window.innerWidth")
            windowInnerHeight = self.driver.execute_script("return window.innerHeight")
            windowScrollX = self.driver.execute_script("return window.scrollX")
            windowScrollY = self.driver.execute_script("return window.scrollY")
            bottonWidth = (windowOuterWidth - windowInnerWidth) / 2
            position[0] += int(windowX + (windowInnerWidth - fatherSize[0]) / 2 - bottonWidth)
            position[1] += int(windowY + (windowOuterHeight - windowInnerHeight - bottonWidth) + (windowInnerHeight - fatherSize[1]) / 2 + 1.5 * bottonWidth)
            self.pyautogui.moveTo(position[0],position[1])
            self.pyautogui.click()
            return position
        except Exception as exception :
            self.globals.debug(f'Failed to return {element}. Cause: {str(exception)}')
