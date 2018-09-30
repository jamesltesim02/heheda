from flask import Flask, request
from werkzeug.routing import BaseConverter
import json
import requests

app = Flask(__name__)

# 正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

# 注册re 转换器  RegexConverter
app.url_map.converters['re'] = RegexConverter

@app.route('/<re(".*"):api_url>', methods=['POST', 'GET'])
def index(api_url):
    method = request.method
    headers = request.headers
    if method == 'POST':
        data = json.dumps(request.get_json())
    else:
        data = request.args

    if api_url.startswith('user/register') :
        from User import register
        res = register(api_url, method, data, headers)
    else :
        from httprequest import httpRequest
        res = httpRequest(api_url, method, data, headers)

    return res

if __name__ == '__main__':
    app.run('192.168.254.102', 5000)
