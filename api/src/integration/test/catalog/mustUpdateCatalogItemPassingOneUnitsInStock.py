testCase:
    createCatalogItem:
        url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
        tag : 'Catalog'
        method : 'createOrUpdateCatalogItem'
        verb : 'POST'
        processingTime:1
        payload : '''{
            "category": "ONU",
            "code": "__10__someCode__10__",
            "name": "__10__someName__10__",
            "patrimonyCode": "__10__somePatrimonyCode__10__",
            "serial": "__10__someSerial__10__",
            "unitsInStock": 1
        }'''
        expectedResponse : '''{
            "importCatalogResponse":{
                "importCatalogResult":{
                    "returnValue":"OK",
                    "rowsImported":1,
                    "rowsRead":1,
                    "data":null,
                    "dataString":"<Items><Item>\n<category>ONU</category>\n<serial>__10__someSerial__10__</serial>\n<patrimonyCode>__10__somePatrimonyCode__10__</patrimonyCode>\n<name>__10__someName__10__</name>\n<code>__10__someCode__10__</code>\n<unitsInStock>1</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
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
            "code": "__10__someCode__10__",
            "name": "__10__otherName__10__",
            "patrimonyCode": "__10__otherPatrimonyCode__10__",
            "serial": "__10__otherSerial__10__",
            "unitsInStock": 0
        }'''
        expectedResponse : '''{
            "importCatalogResponse":{
                "importCatalogResult":{
                    "returnValue":"OK",
                    "rowsImported":1,
                    "rowsRead":1,
                    "data":null,
                    "dataString":"<Items><Item>\n<category>IPTV</category>\n<serial>__10__otherSerial__10__</serial>\n<patrimonyCode>__10__otherPatrimonyCode__10__</patrimonyCode>\n<name>__10__otherName__10__</name>\n<code>__10__someCode__10__</code>\n<unitsInStock>0</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
                    "dataFormat":"XML"
                }
            }
        }'''
