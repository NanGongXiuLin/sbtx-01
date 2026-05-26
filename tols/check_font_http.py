import urllib.request
from urllib.parse import quote
fname = '方正兰亭圆-逐梦星辰.woff2'
url = 'http://localhost:8000/tols/' + quote(fname)
req = urllib.request.Request(url, method='HEAD')
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        print('status', r.status)
        for k,v in r.getheaders():
            if k.lower() in ('content-type','content-length'):
                print(k+':', v)
except Exception as e:
    print('error', e)
