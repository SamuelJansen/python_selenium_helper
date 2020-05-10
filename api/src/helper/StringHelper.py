import Constant as c

def filterJson(json) :
    charactereList = [c.NEW_LINE,c.SPACE,c.BAR_N]
    filteredJson = json
    for charactere in charactereList :
        filteredJson = removeCharactere(charactere,filteredJson)
    return filteredJson

def removeCharactere(charactere,string) :
    filteredString = c.NOTHING.join(string.strip().split(charactere))
    return filteredString.replace(charactere,c.NOTHING)
