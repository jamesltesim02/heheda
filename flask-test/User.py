import requests
import json

def register (url, method, data, headers):
    from httprequest import httpRequest
    print('+++++++++++++++++++++++++++++++++++++++++++++++++ in register 1')

    res = httpRequest(url, method, data, headers)

    print('+++++++++++++++++++++++++++++++++++++++++++++++++ in register 2')
    print(type(headers))


    res1 = requests.get(
        url='http://47.52.97.242:8585/user/find/86/13812345678',
        params={} #,
        # headers=myheader
    )
    
    print('+++++++++++++++++++++++++++++++++++++++++++++++++ in register 3')

    print(res1)
    print(res1.text)

    # profile = httpRequest('user/find/86/13812345678', 'GET', {}, headers)

    # print('--------------------------------profile text:')
    # print(profile.text)
    # print('------------------------------------------------')

    # httpRequest('friendship/invite', 'POST', {'friendId': 3, 'message': 'hehe'}, headers)

    # print('user register success:')
    # print(res)

    return res