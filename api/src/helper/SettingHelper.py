
def getFilteredSetting(setting,globals) :
    if globals.STRING == setting.__class__.__name__ :
        if globals.TRIPLE_SINGLE_QUOTE in setting or globals.TRIPLE_DOUBLE_QUOTE in setting :
            if setting.strip()[0:3] == globals.TRIPLE_SINGLE_QUOTE :
                charactereToFilter = globals.TRIPLE_SINGLE_QUOTE
            else :
                charactereToFilter = globals.TRIPLE_DOUBLE_QUOTE
        elif setting.strip().startswith(globals.SINGLE_QUOTE) or setting.strip().startswith(globals.DOUBLE_QUOTE) :
            if setting.strip()[0:1] == globals.SINGLE_QUOTE :
                charactereToFilter = globals.SINGLE_QUOTE
            else :
                charactereToFilter = globals.DOUBLE_QUOTE
        return setting.replace(charactereToFilter,globals.NOTHING)
    return setting
