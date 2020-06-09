#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:19:06 2020

@author: ex-pc
"""

import shutil
import tempfile
import urllib.request
import requests,bs4

def star(obj):
    if obj.select('section h1')[0].select('span') != []:
        return True
    else:
        return False

def energy(obj):
    print(obj.select('.RightBox .mt20')[0].get_text())
    list = len(obj.select('.RightBox p'))
    if star(obj):   
        #エネルギー名
        print(obj.select('section h1')[0].get_text()+'◇')
        list = list - 1
    else:
        print(obj.select('section h1')[0].get_text())
    #説明文の行数
    
    #行数分だけ繰り返し
    for i in range(0,list):
        weapontext = str(obj.select('.RightBox p')[i])
        list = obj.select('.RightBox p')[i].select('span')
        num = len(list)
        if num != 0:
            for effectnumber in range(0,num):
                rep = list[effectnumber]
                weapontext = weapontext.replace(str(rep),str(rep.get('class')[0])).replace('<p>','').replace('</p>','').replace('<br/>','')
        else:
            weapontext = obj.select('.RightBox p')[i].get_text()
        print(weapontext)
