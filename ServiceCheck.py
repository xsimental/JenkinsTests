import requests
import json


def get_token():
    url='https://exchange.satisfacts.com/api/CSP/getUserJWT'
    params = {"username": "admin@token.com","password": "Z4B@g4sT"}
    r = requests.post(url=url,json=params)
    j = json.loads(r.content)
    return str(j['jwt'])


def test_annual_getoverallsummary():
    url ='https://exchange.satisfacts.com/api/Annual/getOverallSummary'
    params = {"start_date":"2018-07-14","end_date":"2018-08-17","user_id":"39986","survey_id":895,"team_ids":[]}
    auth = 'Bearer '+ get_token()
    headers = {'content-type': 'application/json', 'Authorization': auth }
    r = requests.post(url=url,json=params, headers=headers)
    return r.elapsed.total_seconds()


def test_annual_getcommunitiesrecommendscore():
    url ='https://exchange.satisfacts.com/api/Annual/getCommunitiesRecommendScore'
    params = {"survey_id":895,"start_date":"2018-07-14","end_date":"2018-08-17","team_ids":[]}
    auth = 'Bearer ' + get_token()
    headers = {'content-type': 'application/json', 'Authorization': auth }
    r = requests.post(url=url,json=params, headers=headers)
    return r.elapsed.total_seconds()


def test_insitetrend_getOverallSummary():
    url ='https://exchange.satisfacts.com/api/InsiteTrend/getOverallSummary'
    params = {"client_id":63,"interval":12,"start_date":"2019-01-01","team_ids":[]}
    auth = 'Bearer '+ get_token()
    headers = {'content-type': 'application/json', 'Authorization': auth }
    r = requests.post(url=url,json=params, headers=headers)
    return r.elapsed.total_seconds()

test1 = test_annual_getcommunitiesrecommendscore()
test2 = test_annual_getoverallsummary()
test3 = test_insitetrend_getOverallSummary()
print 'Get Communities Recommend Score (Annual):' + str(test1)
print 'Get Overall Summary (Annual):' + str(test2)
print 'Get Overall Summary (Insite Trend):' + str(test3)
if test1>10:
    raise Exception('Get Communities Recommend Score (Annual) took more than 10 seconds')
if test2>10:
    raise Exception('Get Overall Summary (Annual) took more than 10 seconds')
if test3>10:
    raise Exception('Get Overall Summary (Insite Trend) took more than 10 seconds')





