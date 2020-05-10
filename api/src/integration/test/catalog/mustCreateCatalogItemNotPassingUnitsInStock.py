url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
tag : 'Catalog'
method : 'createOrUpdateCatalogItem'
verb : 'POST'
processingTime:1
payload : '''{
    "category": "IPTV",
    "code": "__2__someCode__2__",
    "name": "__2__someName__2__",
    "patrimonyCode": "__2__somePatrimonyCode__2__",
    "serial": "__2__someSerial__2__"
}'''
expectedResponse : '''{
    "importCatalogResponse":{
        "importCatalogResult":{
            "returnValue":"OK",
            "rowsImported":1,
            "rowsRead":1,
            "data":null,
            "dataString":"<Items><Item>\n<category>IPTV</category>\n<serial>__2__someSerial__2__</serial>\n<patrimonyCode>__2__somePatrimonyCode__2__</patrimonyCode>\n<name>__2__someName__2__</name>\n<code>__2__someCode__2__</code>\n<unitsInStock>1</unitsInStock>\n<limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n<requiresSerialNumber>YES</requiresSerialNumber>\n<mustBeBilled>NO</mustBeBilled>\n<Result>Rowimportedsuccessfully</Result>\n</Item>\n</Items>",
            "dataFormat":"XML"
        }
    }
}'''
