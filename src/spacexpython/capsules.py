import requests
import urldata


def capsules():
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules
    return makeRequest(requestUrl)

def custom(capsule_id):
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + "/" + str(capsule_id)
    return makeRequest(requestUrl)


def makeRequest(requestUrl):
    url_response = requests.get(url=str(requestUrl), timeout=1)
    response = url_response.json()
    return response

