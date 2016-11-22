# -*- coding: utf-8 -*-
import requests
from lxml import etree


def robust(func):
    def decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            print u"sorry, 抓取出错"

    return decorate


@robust
def freeProxyOne(page=5):
    """
    抓取快代理IP http://www.kuaidaili.com/
    :param page: 翻页数
    :return:
    """
    url_list = ('http://www.kuaidaili.com/proxylist/{page}/'.format(page) for page in range(1, page + 1))
    # 页数不用太多， 后面的全是历史IP， 可用性不高
    for url in url_list:
        html = requests.get(url).content
        pass


if __name__ == '__main__':
    f = freeProxyOne()

