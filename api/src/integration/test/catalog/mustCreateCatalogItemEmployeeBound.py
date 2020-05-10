url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
tag : 'Catalog'
method : 'createOrUpdateCatalogItemEmployeeBound'
verb : 'POST'
processingTime : 1
payload : '''{
    "catalogItemRequestDto": {
        "category": "ONU",
        "code": "__5__someCode__5__",
        "name": "__5__someName__5__",
        "patrimonyCode": "__5__somePatrimonyCode__5__",
        "serial": "__5__someSerial__5__",
        "unitsInStock": 1
    },
    "employeeCode": "9999",
    "unitsInEmployeeStock": 1
}'''
expectedResponse : '''{
    "importCatalogAndEmployeeCatalogResponse": {
        "importCatalogAndEmployeeCatalogResult": {
            "returnValue": "OK",
            "rowsImported": 1,
            "rowsRead": 1,
            "data": null,
            "dataString": "<Items>\n  <Item>\n    <category>ONU</category>\n    <serial>__5__someSerial__5__</serial>\n    <patrimonyCode>__5__somePatrimonyCode__5__</patrimonyCode>\n    <name>__5__someName__5__</name>\n    <code>__5__someCode__5__</code>\n    <unitsInStock>1</unitsInStock>\n    <limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n    <requiresSerialNumber>YES</requiresSerialNumber>\n    <mustBeBilled>NO</mustBeBilled>\n    <employeeCode>9999</employeeCode>\n    <unitsInEmployeeStock>1</unitsInEmployeeStock>\n    <Result>Row imported successfully</Result>\n    <Result>Item imported successfully</Result>\n  </Item>\n</Items>",
            "dataFormat": "XML"
        }
    }
}'''
