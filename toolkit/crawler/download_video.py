from urllib import request
from urllib.request import Request

video_url = 'https://v.qq.com/x/page/k004158s3jo.html'
req = Request(video_url)
resp = request.urlopen(req)
bytes = resp.read()
with open('video.mp4', 'wb') as f:
    f.write(bytes)
