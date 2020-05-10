url : 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'
tag : 'Catalog'
method : 'createOrUpdateCatalogItemEmployeeBoundList'
verb : 'POST'
processingTime : 1
payload : '''[
    {
        "catalogItemRequestDto": {
            "category": "ONU",
            "code": "__4__someCode__4__",
            "name": "__4__someName__4__",
            "patrimonyCode": "__4__somePatrimonyCode__4__",
            "serial": "__4__someSerial__4__",
            "unitsInStock": 1
        },
        "employeeCode": "9999",
        "unitsInEmployeeStock": 1
    },
    {
        "catalogItemRequestDto": {
            "category": "IPTV",
            "code": "__4__someOtherCode__4__",
            "name": "__4__someOtherName__4__",
            "patrimonyCode": "__4__someOtherPatrimonyCode__4__",
            "serial": "__4__someOtherSerial__4__",
            "unitsInStock": 0
        },
        "employeeCode": "9999",
        "unitsInEmployeeStock": 0
    }
]'''
expectedResponse : '''{
    "importCatalogAndEmployeeCatalogResponse": {
        "importCatalogAndEmployeeCatalogResult": {
            "returnValue": "OK",
            "rowsImported": 2,
            "rowsRead": 2,
            "data": null,
            "dataString": "<Items>\n  <Item>\n    <category>ONU</category>\n    <serial>__4__someSerial__4__</serial>\n    <patrimonyCode>__4__somePatrimonyCode__4__</patrimonyCode>\n    <name>__4__someName__4__</name>\n    <code>__4__someCode__4__</code>\n    <unitsInStock>1</unitsInStock>\n    <limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n    <requiresSerialNumber>YES</requiresSerialNumber>\n    <mustBeBilled>NO</mustBeBilled>\n    <employeeCode>9999</employeeCode>\n    <unitsInEmployeeStock>1</unitsInEmployeeStock>\n    <Result>Row imported successfully</Result>\n    <Result>Item imported successfully</Result>\n  </Item>\n  <Item>\n    <category>IPTV</category>\n    <serial>__4__someOtherSerial__4__</serial>\n    <patrimonyCode>__4__someOtherPatrimonyCode__4__</patrimonyCode>\n    <name>__4__someOtherName__4__</name>\n    <code>__4__someOtherCode__4__</code>\n    <unitsInStock>0</unitsInStock>\n    <limitQuantityInMultiplesOf>1</limitQuantityInMultiplesOf>\n    <requiresSerialNumber>YES</requiresSerialNumber>\n    <mustBeBilled>NO</mustBeBilled>\n    <employeeCode>9999</employeeCode>\n    <unitsInEmployeeStock>0</unitsInEmployeeStock>\n    <Result>Row imported successfully</Result>\n    <Result>Item imported successfully</Result>\n  </Item>\n</Items>",
            "dataFormat": "XML"
        }
    }
}'''
