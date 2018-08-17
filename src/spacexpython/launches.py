import requests
import urldata



def launches():
    requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def latest():
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def next():
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

def upcoming():
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response
