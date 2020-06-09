#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:13:03 2020

@author: ex-pc
"""
import shutil
import tempfile
import urllib.request
import requests,bs4

def goods(obj):
    #なぞの化石の場合トレーナーになっているのでグッズに変更
    if (obj.select('.RightBox .mt20')[0].get_text() == 'トレーナー'):
        print('グッズ')
    else:
        print(obj.select('.RightBox .mt20')[0].get_text())

    #グッズ名
    print(obj.select('section h1')[0].get_text())
    #説明文の行数
    list = len(obj.select('.RightBox p'))
    #行数分だけ繰り返し(グッズの基本ルールはカット)
    print('begin_effect')
    for effect in range(0,list-1):
        effecttext = str(obj.select('.RightBox p')[effect])
        list = obj.select('.RightBox p')[effect].select('span')
        num = len(list)
        if num != 0:
            for effectnumber in range(0,num):
                rep = list[effectnumber]
                effecttext = effecttext.replace(str(rep),str(rep.get('class')[0])).replace('<p>','').replace('</p>','').replace('<br/>','')
        else:
            effecttext = obj.select('.RightBox p')[effect].get_text()
        print(effecttext)
    print('end_effect')

