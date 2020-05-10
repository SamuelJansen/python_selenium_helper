def runTestSet(swagger,testSet) :
    globals = swagger.globals
    for tag in testSet.keys() :
        for testName in testSet[tag] :
            testCase = swagger.getTestCase(tag,testName)
            for testCaseKey,testCaseValues in testCase.items() :
                runTestCase(swagger,testCaseKey,testCaseValues)

def runTestCase(swagger,testCaseKey,testCaseValues) :
    url = swagger.getFilteredSetting('url',testCaseValues)
    tag = swagger.getFilteredSetting('tag',testCaseValues)
    method = swagger.getFilteredSetting('method',testCaseValues)
    verb = swagger.getFilteredSetting('verb',testCaseValues)
    processingTime = swagger.getFilteredSetting('processingTime',testCaseValues)
    payload = swagger.getFilteredSetting('payload',testCaseValues)
    expectedResponse =swagger.getFilteredSetting('expectedResponse',testCaseValues)
    response,success = swagger.runTest(url,tag,method,verb,processingTime,payload,expectedResponse)
    print(f'''
        {testCaseKey}''',end='')
    if success :
        print(f'''
            Success''')
    else :
        print(f'''
            url = {url}
            tag = {tag}
            method = {method}
            verb = {verb}
            processingTime = {processingTime}
            payload = {payload}
            expectedResponse = {expectedResponse}
            response = {response}''')
