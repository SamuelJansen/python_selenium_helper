if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SwaggerIntegration
    swagger = SwaggerIntegration.SwaggerIntegration(globals)

    runTestSet = {
        'Catalog' : [
            'mustCreateCatalogItemPassingOneUnitsInStock',
            'mustCreateCatalogItemNotPassingUnitsInStock',
            'mustCreateCatalogItemPassingZeroUnitsInStock',

            'mustUpdateCatalogItemPassingOneUnitsInStock',
            'mustUpdateCatalogItemNotPassingUnitsInStock',
            'mustUpdateCatalogItemPassingZeroUnitsInStock',

            'mustCreateCatalogItemEmployeeBound',
            'mustCreateCatalogItemEmployeeBoundList'
        ]
    }

    swagger.runTestSet(runTestSet)

    swagger.closeDriver()
