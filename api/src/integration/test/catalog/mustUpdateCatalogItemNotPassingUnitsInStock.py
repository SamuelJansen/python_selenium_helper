testCase:
    createCatalogItem:
        url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
        tag : 'Catalog'
        method : 'createOrUpdateCatalogItem'
        verb : 'POST'
        processingTime:1
        payload : '''{
            "category": "IPTV",
            "code": "__12__someCode__12__",
            "name": "__12__someName__12__",
            "patrimonyCode": "__12__somePatrimonyCode__12__",
            "serial": "__12__someSerial__12__",
            "unitsInStock": "0"
        }'''
        expectedResponse : '''{
            "importCatalogResponse":{
                "importCatalogResult":{
                    "returnValue":"OK",
                    "rowsImported":1,
                    "rowsRead":1,
                    "data":null,
                    "dataString":"<Items><Item>\n<category>IPTV</category>\n<serial>__12__someSerial__12__</serial>\n<patrimonyCode>__12__somePatrimonyCode__12__</patrimonyCode>\n<name>__12__someName__12__</name>\n<code>__12__someCode__12__</code>\n<unitsInStock>0</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
                    "dataFormat":"XML"
                }
            }
        }'''
    updateCatalogItem:
        url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
        tag : 'Catalog'
        method : 'createOrUpdateCatalogItem'
        verb : 'POST'
        processingTime:1
        payload : '''{
            "category": "ONU",
            "code": "__12__someCode__12__",
            "name": "__12__otherName__12__",
            "patrimonyCode": "__12__otherPatrimonyCode__12__",
            "serial": "__12__otherSerial__12__"
        }'''
        expectedResponse : '''{
            "importCatalogResponse":{
                "importCatalogResult":{
                    "returnValue":"OK",
                    "rowsImported":1,
                    "rowsRead":1,
                    "data":null,
                    "dataString":"<Items><Item>\n<category>ONU</category>\n<serial>__12__otherSerial__12__</serial>\n<patrimonyCode>__12__otherPatrimonyCode__12__</patrimonyCode>\n<name>__12__otherName__12__</name>\n<code>__12__someCode__12__</code>\n<unitsInStock>1</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
                    "dataFormat":"XML"
                }
            }
        }'''
