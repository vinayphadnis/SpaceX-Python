import requests
import urldata


def rockets():
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets
    return makeRequest(requestUrl)

def falcon1():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_1
    return makeRequest(requestUrl)

def falcon9():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_9
    return makeRequest(requestUrl)

def falconHeavy():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_heavy
    return makeRequest(requestUrl)

def bfr():
    requestUrl = urldata.Domain.main + urldata.Domain.big_falcon_rocket
    return makeRequest(requestUrl)

def makeRequest(requestUrl):
    url_response = requests.get(url=str(requestUrl), timeout=1)
    response = url_response.json()
    return response