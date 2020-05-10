import SeleniumAbstractor, ObjectHelper, SwaggerTestRunner, SettingHelper

class SwaggerIntegration(SeleniumAbstractor.SeleniumAbstractor):

    def __init__(self,pathMannanger):

        SeleniumAbstractor.SeleniumAbstractor.__init__(self,pathMannanger)

        self.EXPAND_OPERATION = 'expand-operation'
        self.TRY_OUT = 'try-out'
        self.BODY_PARAM = 'body-param__text'
        self.EXECUTE_WRAPPER = 'execute-wrapper'
        self.HIGHLIGHT_CODE = 'highlight-code'
        self.MICROLIGHT = 'microlight'
        self.TEST_CASE = 'testCase'

        self.integrationPath = 'integration\\test\\'

    def runTestSet(self,testSet):
        SwaggerTestRunner.runTestSet(self,testSet)

    def runTest(self,url,tag,method,verb,processingTime,payload,expectedResponse) :
        self.resetValues(url,tag,method,verb,processingTime,payload,expectedResponse)
        swaggerUrl = self.accessSwaggerUrl()
        swaggerTag = self.accessTag(swaggerUrl)
        swaggerMethod = self.accessMethod(swaggerTag)
        self.hitTryOut(swaggerMethod)
        self.typePayload(swaggerMethod)
        self.hitExecute(swaggerMethod)
        self.waitProcessingTime()
        response = self.getResponse(swaggerMethod)
        return response,ObjectHelper.equal(response,expectedResponse)

    def resetValues(self,url,tag,method,verb,processingTime,payload,expectedResponse):
        self.url = url
        self.tag = tag
        self.method = method
        self.verb = verb
        self.processingTime = processingTime
        self.payload = payload
        self.expectedResponse = expectedResponse
        self.findByIdRequest = f'operations-tag-{self.tag}'
        self.accessIdRequest = f'operations-{self.tag}-{self.method}Using{self.verb}'

    def accessSwaggerUrl(self):
        return self.accessUrl(self.url)

    def accessTag(self,swaggerUrl):
        return self.accessClass(self.EXPAND_OPERATION,self.findById(self.findByIdRequest,swaggerUrl))

    def accessMethod(self,swaggerTag):
        return self.accessId(self.accessIdRequest,swaggerTag)

    def hitTryOut(self,swaggerMethod):
        self.accessButton(self.findByClass(self.TRY_OUT,swaggerMethod))

    def typePayload(self,swaggerMethod):
        self.typeInSwagger(self.payload,self.findByClass(self.BODY_PARAM,swaggerMethod))

    def hitExecute(self,swaggerMethod):
        self.accessButton(self.findByClass(self.EXECUTE_WRAPPER,swaggerMethod))

    def getResponse(self,swaggerMethod):
        return self.getTextByClass(self.MICROLIGHT,self.findByClass(self.HIGHLIGHT_CODE,swaggerMethod))

    def waitProcessingTime(self):
        self.wait(processingTime=self.processingTime)

    def getFilteredSetting(self,keySetting,testCase):
        return SettingHelper.getFilteredSetting(self.globals.getSetting(keySetting,testCase),self.globals)
        
    def getTestCase(self,tag,testName):
        settingTree = self.globals.getSettingTree(settingFilePath=f'{self.globals.apiPath}{self.globals.baseApiPath}{self.integrationPath}{tag}{self.globals.BACK_SLASH}{testName}.{self.globals.extension}')
        if self.TEST_CASE in settingTree.keys() :
            newSettingTree = {}
            for settingTreeKey, settingTreeValue in settingTree[self.TEST_CASE].items() :
                newSettingTree[f'{testName}.{settingTreeKey}'] = settingTreeValue
            return newSettingTree
        return {testName : settingTree}
