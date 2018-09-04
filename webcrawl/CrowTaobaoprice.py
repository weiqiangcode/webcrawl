# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:47:05 2018

@author: Administrator
"""

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        for i in range(len(tlt)):
            title = eval(tlt[i].split(':')[1])
            price = eval(plt[i].split(':')[1])
            ilt.append([title, price])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "商品名称", "价格"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 2
    start_url = 'http://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
    
main()