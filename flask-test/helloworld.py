from flask import Flask, request
from werkzeug.routing import BaseConverter
import json
import requests

app = Flask(__name__)

#47.52.97.242:8585

# 正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

# 注册re 转换器  RegexConverter
app.url_map.converters['re'] = RegexConverter

imurl = 'http://47.52.97.242:8585/'

@app.route('/<re(".*"):api_url>', methods=['POST', 'GET'])
def hello_world(api_url):
    url = '%s%s' % (imurl,api_url)

    if request.method == 'GET' :
        res = requests.get(
            url=url,
            headers=request.headers
        )
    else :
        data = json.dumps(request.get_json())
        res = requests.post(
            url=url,
            data=data,
            headers=request.headers
        )

    myheader = {}
    for k in res.headers:
        myheader[k] = res.headers[k]

    return res.text, 200, myheader

if __name__ == '__main__':
    app.run('192.168.254.102', 5000)
