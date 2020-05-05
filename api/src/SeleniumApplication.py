if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger(printStatus = False)

    import Selenium, time
    s = Selenium.Selenium(pathMannanger)

    def accessSwagger(home,tag,method,verb) :
        findById = f'operations-tag-{tag}'
        accessClass = 'expand-operation'
        accessId = f'operations-{tag}-{method}Using{verb}'
        s.accessId(accessId,s.accessClass(accessClass,s.findById(findById,s.accessUrl(home))))



    home = 'https://api03-homologacao.sumicity.net.br:8090/sumicity-officetrack-api/swagger-ui.html'

    tag = 'Catalog'
    method = 'createOrUpdateCatalogItemEmployeeBound'
    verb = 'POST'
    accessSwagger(home,tag,method,verb)
    time.sleep(10)

    tag = 'Catalog'
    method = 'createOrUpdateCatalogItem'
    verb = 'POST'
    accessSwagger(home,tag,method,verb)
    time.sleep(10)
