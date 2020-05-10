url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
tag : 'Catalog'
method : 'createOrUpdateCatalogItem'
verb : 'POST'
processingTime:1
payload : '''{
    "category": "ONU",
    "code": "__1__someCode__1__",
    "name": "__1__someName__1__",
    "patrimonyCode": "__1__somePatrimonyCode__1__",
    "serial": "__1__someSerial__1__",
    "unitsInStock": 1
}'''
expectedResponse : '''{
    "importCatalogResponse":{
        "importCatalogResult":{
            "returnValue":"OK",
            "rowsImported":1,
            "rowsRead":1,
            "data":null,
            "dataString":"<Items><Item>\n<category>ONU</category>\n<serial>__1__someSerial__1__</serial>\n<patrimonyCode>__1__somePatrimonyCode__1__</patrimonyCode>\n<name>__1__someName__1__</name>\n<code>__1__someCode__1__</code>\n<unitsInStock>1</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
            "dataFormat":"XML"
        }
    }
}'''
