import requests
import urldata



def launches():
    requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    return makeRequest(requestUrl)

def latest():
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    return makeRequest(requestUrl)

def next():
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    return makeRequest(requestUrl)

def upcoming():
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    return makeRequest(requestUrl)

def makeRequest(requestUrl):
    url_response = requests.get(url=str(requestUrl), timeout=1)
    response = url_response.json()
    return response
