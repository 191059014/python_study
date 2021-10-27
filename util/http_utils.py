import requests


class HttpRequest:
    """
    http请求
    """

    def __init__(self, method, url, params=None, body=None, headers=None):
        self.method = method
        self.url = url
        self.params = params
        self.body = body
        self.headers = headers

    def execute(self):
        method = self.method
        url = self.url
        params = self.params
        body = self.body
        headers = self.headers
        return requests.request(method, url, params=params, data=body, headers=headers)


class Get(HttpRequest):
    """
    get请求
    """

    def __init__(self, url, params=None, headers=None):
        super(Get, self).__init__('get', url, params, None, headers)


class Post(HttpRequest):
    """
    post请求
    """

    def __init__(self, url, params=None, body=None, headers=None):
        super(Post, self).__init__('post', url, params, body, headers)


if __name__ == "__main__":
    get_resp = Get('http://localhost:8080/testGet', params={'name': 'zhangsan'}, headers={'token': '123'}).execute()
    print("请求地址：", get_resp.url)
    print("请求成功标志：", get_resp.ok)
    print("响应状态码：", get_resp.status_code)
    print("响应头：", get_resp.headers)
    print("响应信息：", get_resp.text)

    get_resp = Post('http://localhost:8080/testPost', params={'name': 'zhangsan'}, body={'password': '123'},
                    headers={'token': '123'}).execute()
    print("请求地址：", get_resp.url)
    print("请求成功标志：", get_resp.ok)
    print("响应状态码：", get_resp.status_code)
    print("响应头：", get_resp.headers)
    print("响应信息：", get_resp.text)
