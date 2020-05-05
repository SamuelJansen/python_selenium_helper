NEW_LINE = '''\n'''
BAR_N = '''\\n'''
SPACE = ''' '''
NOTHING = ''

def runSwagger(home,tag,method,verb,processingTime,payload,expectedResponse) :
    findByIdRequest = f'operations-tag-{tag}'
    expandOperation = 'expand-operation'
    accessIdRequest = f'operations-{tag}-{method}Using{verb}'
    tryOut = 'try-out'
    bodyParam = 'body-param__text'
    executeWrapper = 'execute-wrapper'
    highlightCode = 'highlight-code'
    microlight = 'microlight'
    methodBody = s.accessId(accessIdRequest,s.accessClass(expandOperation,s.findById(findByIdRequest,s.accessUrl(home))))
    s.accessButton(s.findByClass(tryOut,methodBody))
    s.typeInSwagger(payload,s.findByClass(bodyParam,methodBody))
    s.accessButton(s.findByClass(executeWrapper,methodBody))
    wait(processingTime)
    response = s.getTextByClass(microlight,s.findByClass(highlightCode,methodBody))
    return equal(response,expectedResponse)

def equal(response,expectedResponse) :
    filteredResponse = filterJson(response)
    filteredExpectedResponse = filterJson(expectedResponse)
    return filteredResponse == filteredExpectedResponse

def filterJson(json) :
    filteredJson = NOTHING.join(json.strip().split(NEW_LINE))
    filteredJson = NOTHING.join(filteredJson.strip().split(SPACE))
    filteredJson = NOTHING.join(filteredJson.strip().split(BAR_N))
    filteredJson = filteredJson.replace(NEW_LINE,NOTHING)
    filteredJson = filteredJson.replace(SPACE,NOTHING)
    filteredJson = filteredJson.replace(BAR_N,NOTHING)
    return filteredJson

def wait(processingTime) :
    time.sleep(processingTime)

if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger(printStatus = False)

    import Selenium, time
    s = Selenium.Selenium(pathMannanger)

    home = 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
    tag = 'Catalog'
    method = 'createOrUpdateCatalogItem'
    verb = 'POST'
    processingTime = 1
    payload = '''{
        "category": "ONU",
        "code": "__someCode__",
        "name": "__someName__",
        "patrimonyCode": "__somePatrimonyCode__",
        "serial": "__someSerial__",
        "unitsInStock": 1
    }'''
    expectedResponse = '''{
        "importCatalogResponse":{
            "importCatalogResult":{
                "returnValue":"OK",
                "rowsImported":1,
                "rowsRead":1,
                "data":null,
                "dataString":"<Items><Item>\n<category>ONU</category>\n<serial>__someSerial__</serial>\n<patrimonyCode>__somePatrimonyCode__</patrimonyCode>\n<name>__someName__</name>\n<code>__someCode__</code>\n<unitsInStock>1</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
                "dataFormat":"XML"
            }
        }
    }'''
    success = runSwagger(home,tag,method,verb,processingTime,payload,expectedResponse)
    print(f'Success = {success}')

    home = 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
    tag = 'Catalog'
    method = 'createOrUpdateCatalogItemEmployeeBound'
    verb = 'POST'
    processingTime = 1
    payload = '''{
        "catalogItemRequestDto": {
            "category": "ONU",
            "code": "__someCode__",
            "name": "__someName__",
            "patrimonyCode": "__somePatrimonyCode__",
            "serial": "__someSerial__",
            "unitsInStock": 1
        },
        "employeeCode": "9999",
        "unitsInEmployeeStock": 1
    }'''
    expectedResponse = '''{
        "importCatalogAndEmployeeCatalogResponse": {
            "importCatalogAndEmployeeCatalogResult": {
                "returnValue": "OK",
                "rowsImported": 1,
                "rowsRead": 1,
                "data": null,
                "dataString": "<Items>\n  <Item>\n    <category>ONU</category>\n    <serial>__someSerial__</serial>\n    <patrimonyCode>__somePatrimonyCode__</patrimonyCode>\n    <name>__someName__</name>\n    <code>__someCode__</code>\n    <unitsInStock>1</unitsInStock>\n    <limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n    <requiresSerialNumber>YES</requiresSerialNumber>\n    <mustBeBilled>NO</mustBeBilled>\n    <employeeCode>9999</employeeCode>\n    <unitsInEmployeeStock>1</unitsInEmployeeStock>\n    <Result>Row imported successfully</Result>\n    <Result>Item imported successfully</Result>\n  </Item>\n</Items>",
                "dataFormat": "XML"
            }
        }
    }'''
    success = runSwagger(home,tag,method,verb,processingTime,payload,expectedResponse)
    print(f'Success = {success}')

    s.closeDriver()
