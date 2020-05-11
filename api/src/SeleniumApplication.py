if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SeleniumAbstractor
    selenium = SeleniumAbstractor.SeleniumAbstractor(globals)
    selenium.closeDriver()
