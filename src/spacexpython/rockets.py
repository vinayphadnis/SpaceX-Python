import requests
import urldata


def rockets():
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def falcon1():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_1
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def falcon9():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_9
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def falconHeavy():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_heavy
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def bfr():
    requestUrl = urldata.Domain.main + urldata.Domain.big_falcon_rocket
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response