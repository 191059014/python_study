import webbrowser

source_url = 'http://www.wmxz.wang/video.php?url='
print('输入想看的vip的视频地址：')
video_url = input()
webbrowser.open(source_url + video_url)
