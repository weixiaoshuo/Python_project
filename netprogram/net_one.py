# python网络编程 客户端编程 这里只介绍request库的使用

import requests  # 开源库requests
import urllib.request, urllib.response ,urllib.parse
# python3 使用urllib模块python2迁移过来的

res = urllib.parse.urlparse('http://www.baidu.com');
print(res)

response = requests.get('http://www.baidu.com')
print(response.content)
