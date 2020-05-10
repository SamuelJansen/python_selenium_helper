import StringHelper

def equal(response,expectedResponse) :
    filteredResponse = StringHelper.filterJson(response)
    filteredExpectedResponse = StringHelper.filterJson(expectedResponse)
    return filteredResponse == filteredExpectedResponse
