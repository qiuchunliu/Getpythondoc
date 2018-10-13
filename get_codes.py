# get python docs

import requests
from bs4 import BeautifulSoup
import os
# 创建文件夹写入 .txt 文件

os.mkdir(r'C:\Users\qiuchunliu\Desktop\doc')


def get_html_soup(url):
    ht = requests.get(url)
    ht.encoding = ht.apparent_encoding
    htx = ht.text
    # print(htx)
    return BeautifulSoup(htx, 'html.parser')
# 解析目标网页，返回解析后的文件


def get_headdoc(url):
    htmls = get_html_soup(url)
    tutorial = htmls.find_all('div', attrs={'id': "the-python-tutorial"})
    # 使用 标签名 和 属性键值对 来匹配标签
    tex = tutorial[0]
    with open(r'C:\Users\qiuchunliu\Desktop\doc\no_head_doc.txt', 'w', encoding='utf-8') as headdoc:
        headdoc.write(tex.text)
# 输出开头文档


def get_links(url):
    title = []
    links = []
    href = get_html_soup(url).find_all('div', attrs={'class': "toctree-wrapper compound"})
    for link in href[0].ul.find_all('li', attrs={'class': "toctree-l1"}):
        title.append(link.a.text)
        links.append('https://docs.python.org/3/tutorial/' + link.a.get('href'))
    zipp = zip(title, links)
    dic_links = dict(zipp)
    return dic_links
# 获取每个章节的链接


def get_docs(url):
    n = 1
    url_dic = get_links(url)
    for key in url_dic:
        url = url_dic[key]
        ht = requests.get(url)
        ht.encoding = ht.apparent_encoding
        hts = BeautifulSoup(ht.text, 'html.parser')
        doc = hts.find_all('div', attrs={'class': "body"})
        with open(r'C:\Users\qiuchunliu\Desktop\doc\no_%d_doc.txt' % n, 'w', encoding='utf-8') as docc:
            docc.write(doc[0].div.text)
        n += 1
# 根据链接，获取每个章节的文本内容，并写在 .txt 文件内
# 此时将 div.text 写入文本文件内，会出现编码不匹配的报错，需要再加入 encoding = 'utf-8'


def main(url):
    get_html_soup(url)
    get_headdoc(url)
    get_links(url)
    get_docs(url)


if __name__ == '__main__':
    urll = 'https://docs.python.org/3/tutorial/index.html'
    main(urll)
    # 给出 python.doc 的链接并且得出结果
