import requests
import json

def gotest(temp):
    url = "http://localhost:2333/user_story/similar"


    payload = "{\"title\":\"\",\"body\":\"" + temp + "\"}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.16.3",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4d26206c-244f-459c-bfcb-59937ee38225,de138585-b05e-40ea-8350-413291ff6514",
        'Host': "localhost:2333",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "310",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    res = result[0]['body']


    return res