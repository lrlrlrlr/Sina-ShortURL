#!/usr/bin/env python
#coding:utf-8
"""
  Author:  yafeile --<yafeile@163.com>
  Purpose: 
  Created: Tuesday, March 15, 2016
"""

from urllib2 import Request, urlopen, build_opener, HTTPCookieProcessor, install_opener
from urlparse import urljoin, urlparse
from urllib import urlencode, unquote
from base64 import b64encode
from json import loads
from cookielib import CookieJar

TYPES = {
    "sina.it": "sinalt",
    "t.cn": "sina",
    "dwz.cn": "dwz",
    "qq.cn.hn": "qq.cn.hn",
    "tb.cn.hn": "tb.cn.hn",
    "jd.cn.hn": "jd.cn.hn",
    "tinyurl.com": "tinyurl",
    "qr.net": "qr",
    "goo.gl": "googl",
    "is.gd": "isgd",
    "j.mp": "jmp",
    "bit.ly": "bitly",
}

def generate(url, suffix = None):
    """生成新浪的短链接"""
    scheme = urlparse(url).scheme
    if not scheme:
        url = 'http://' + url
    host = "http://dwz.wailian.work"
    site = TYPES.get(suffix, "sina")
    url = b64encode(url)
    params = [("url", url), ("site", site)]
    params = unquote(urlencode(params))
    url = urljoin(host, "api.php?{0}".format(params))
    headers= [
        ("Accept", "application/json,text/javascript,*/*;q=0.01"),
        ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0"),
        ("Referer", 'dwz.wailian.work'),
        ("Connection", "keep-alive")
    ]
    cookie = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie))
    opener.addheaders = headers
    f = opener.open(host).read()
    f = opener.open(url)
    data = f.read()
    if data:
        data = loads(data)
    status = data['result']
    if status.lower() == 'ok':
        return data['data']
    else:
        return 'Error:'.format(data['data'])
    
if __name__ == '__main__':
    print generate('https://www.baidu.com', suffix="sina.it")