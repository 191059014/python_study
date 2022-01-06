import threading

import requests

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
PROXYS = [
    {'http': '220.173.37.128:7890'},
    {'http': '118.180.166.195:8060'},
    {'http': '120.26.160.120:7890'},
    {'http': '139.9.2.31:8081'},
    {'http': '14.20.235.129:34100'},
    {'http': '58.20.235.180:9091'},
    {'http': '118.180.166.195:8060'},
    {'http': '47.92.234.75:80'},
    {'http': '47.56.69.11:8000'},
    {'http': '183.247.211.151:30001'},
    {'http': '180.97.87.63:80'},
    {'http': '111.3.118.247:30001'},
    {'http': '221.125.138.189:8380'},
    {'http': '47.106.105.236:80'},
    {'http': '218.75.102.198:8000'},
    {'http': '152.136.62.181:9999'},
    {'http': '47.243.190.108:7890'},
    {'http': '115.235.18.113:9000'},
    {'http': '183.23.72.86:3128'},
    {'http': '117.114.149.66:55443'}
]


def invoke(proxy):
    url = "https://www.mcmssc.com/0_69/41890.html"
    resp = requests.get(url, headers={'User-Agent': USER_AGENT}, proxies=proxy)
    status_code = resp.status_code
    if status_code != 200:
        print("code: " + str(status_code) + ', message: ' + resp.reason + ", " + url + ", " + str(proxy))


for proxy in PROXYS:
    threading.Thread(target=invoke, args=(proxy,)).start()
