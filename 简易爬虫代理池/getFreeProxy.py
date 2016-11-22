# -*- coding: utf-8 -*-
import requests
from lxml import etree


def robust(func):
    def decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print u"sorry, 抓取出错。错误原因:"
            print e

    return decorate


# 快代理
# noinspection PyPep8Naming
@robust
def freeProxyOne(page=10):
    """
    抓取快代理IP http://www.kuaidaili.com/
    :param page: 翻页数
    :return:
    """
    url_list = ('http://www.kuaidaili.com/proxylist/{page}/'.format(page=page) for page in range(1, page + 1))
    # 页数不用太多， 后面的全是历史IP， 可用性不高
    for url in url_list:
        html = requests.get(url).content
        tree = etree.HTML(html)
        proxy_list = tree.xpath('.//div[@id="index_free_list"]//tbody/tr')
        for proxy in proxy_list:
            yield ':'.join(proxy.xpath('./td/text()')[0:2])

if __name__ == '__main__':
    for e in freeProxyOne():
        print e

