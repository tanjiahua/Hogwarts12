

import requests

def test_baidu():
    res = requests.get('http://www.baidu.com')
    print(res.status_code)



test_baidu()