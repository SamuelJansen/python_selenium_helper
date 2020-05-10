testCase:
    createCatalogItem:
        url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
        tag : 'Catalog'
        method : 'createOrUpdateCatalogItem'
        verb : 'POST'
        processingTime:1
        payload : '''{
            "category": "ONU",
            "code": "__11__someCode__11__",
            "name": "__11__someName__11__",
            "patrimonyCode": "__11__somePatrimonyCode__11__",
            "serial": "__11__someSerial__11__",
            "unitsInStock": 0
        }'''
        expectedResponse : '''{
            "importCatalogResponse":{
                "importCatalogResult":{
                    "returnValue":"OK",
                    "rowsImported":1,
                    "rowsRead":1,
                    "data":null,
                    "dataString":"<Items><Item>\n<category>ONU</category>\n<serial>__11__someSerial__11__</serial>\n<patrimonyCode>__11__somePatrimonyCode__11__</patrimonyCode>\n<name>__11__someName__11__</name>\n<code>__11__someCode__11__</code>\n<unitsInStock>0</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
                    "dataFormat":"XML"
                }
            }
        }'''
    uptadeCatalogItem:
        url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
        tag : 'Catalog'
        method : 'createOrUpdateCatalogItem'
        verb : 'POST'
        processingTime:1
        payload : '''{
            "category": "IPTV",
            "code": "__11__someCode__11__",
            "name": "__11__otherName__11__",
            "patrimonyCode": "__11__otherPatrimonyCode__11__",
            "serial": "__11__otherSerial__11__",
            "unitsInStock": 1
        }'''
        expectedResponse : '''{
            "importCatalogResponse":{
                "importCatalogResult":{
                    "returnValue":"OK",
                    "rowsImported":1,
                    "rowsRead":1,
                    "data":null,
                    "dataString":"<Items><Item>\n<category>IPTV</category>\n<serial>__11__otherSerial__11__</serial>\n<patrimonyCode>__11__otherPatrimonyCode__11__</patrimonyCode>\n<name>__11__otherName__11__</name>\n<code>__11__someCode__11__</code>\n<unitsInStock>1</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
                    "dataFormat":"XML"
                }
            }
        }'''
