if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SeleniumHelper
    selenium = SeleniumHelper.SeleniumHelper(globals)
    selenium.closeDriver()
