import threading

import requests

from toolkit.crawler.spider import USER_AGENT, PROXYS


def invoke(proxy):
    url = "https://read.qidian.com/chapter/MUNxpctET5IuTkiRw_sFYA2/16ZAmnHutABOBDFlr9quQA2/"
    resp = requests.get(url, headers={'User-Agent': USER_AGENT}, proxies=proxy)
    status_code = resp.status_code
    if status_code != 200:
        print("code: " + str(status_code) + ', message: ' + resp.reason + ", " + url + ", " + str(proxy))
    else:
        print("code: " + str(status_code) + ", " + url + ", " + str(proxy))


for proxy in PROXYS:
    threading.Thread(target=invoke, args=(proxy,)).start()
