import json
import requests

imurl = 'http://47.52.97.242:8585/'

def httpRequest (api_url, method, data, headers):
    url = '%s%s' % (imurl,api_url)

    print('request url:')
    print(url)
    print('request data:')
    print(data)
    print('request headers:')
    print(headers)

    if method == 'GET' :
        res = requests.get(
            url=url,
            params=data,
            headers=headers
        )
    else :
        res = requests.post(
            url=url,
            data=data,
            headers=headers
        )

    print('result status code:')
    print(res.status_code)
    print('result content:')
    print(res.text)

    myheader = {}
    for k in res.headers:
        myheader[k] = res.headers[k]

    return res.text, res.status_code, myheader