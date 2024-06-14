import requests
import json
import base64


def main():
    ak = "hPNmSC7FW1IHZ8yqWMvXTUiK"
    sk = "y4VQy6IjmMn9isRyUxOEDY9WD7ZHD7Kt"
    url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    access_token = response.json()['access_token']
    print('access_token', access_token)
    return access_token

main()


'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open(r'E:\重汽代码\ocr_program\demo1\四轮定位1.png', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = main()
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())


