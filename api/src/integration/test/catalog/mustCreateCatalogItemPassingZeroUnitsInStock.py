url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
tag : 'Catalog'
method : 'createOrUpdateCatalogItem'
verb : 'POST'
processingTime:1
payload : '''{
    "category": "ONU",
    "code": "__3__someCode__3__",
    "name": "__3__someName__3__",
    "patrimonyCode": "__3__somePatrimonyCode__3__",
    "serial": "__3__someSerial__3__",
    "unitsInStock": 0
}'''
expectedResponse : '''{
    "importCatalogResponse":{
        "importCatalogResult":{
            "returnValue":"OK",
            "rowsImported":1,
            "rowsRead":1,
            "data":null,
            "dataString":"<Items><Item>\n<category>ONU</category>\n<serial>__3__someSerial__3__</serial>\n<patrimonyCode>__3__somePatrimonyCode__3__</patrimonyCode>\n<name>__3__someName__3__</name>\n<code>__3__someCode__3__</code>\n<unitsInStock>0</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
            "dataFormat":"XML"
        }
    }
}'''
