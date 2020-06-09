import requests
import re
import uuid
import pokemon
import goods
import suport
import energy
import stadium

from bs4 import BeautifulSoup

#promo_list = {35391,35394,35397,36144,36145,36216,36428,36429,36895,36898,37064,37179,37182,37186,37189,37194}

#スクレイピングするパックの最初のカードのidをf_minに、最後のカードのidをf_maxに設定
f_min = 37179
f_max = 37182
#パックの名称をpackに設定
pack = 's3'

for url_number in range(f_min,f_max+1):
#for url_number in promo_list:
    #for ループ内でカード毎にアクセス
    url = "https://www.pokemon-card.com/card-search/details.php/card/"+str(url_number)+"/regu/XY"
    get_url_info = requests.get(url)
    bs4obj = BeautifulSoup(get_url_info.text, 'lxml')
    if bs4obj.select('.RightBox .mt20')[0].get_text() != '':
            #ポケモン、グッズ、ポケモンのどうぐ、サポート、スタジアム、基本エネルギー、特殊エネルギーで処理ファイル分け
            if bs4obj.select('.RightBox .mt20')[0].get_text() == 'グッズ':    
                goods.goods(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'ポケモンのどうぐ':
                goods.goods(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'サポート':
                suport.suport(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'スタジアム':
                stadium.stadium(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == '基本エネルギー':
                energy.energy(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == '特殊エネルギー':
                energy.energy(bs4obj)
            #なぞの化石がページバグでトレーナーになっているため例外として処理
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'トレーナー':
                goods.goods(bs4obj)
            #ポケモンだけこの要素がポケモン名になっているためelseで処理
            else:
                pokemon.pokemon(bs4obj)

            print(url_number)
            print(pack)
            print('/')

            #テキストに対応するカード画像も取得
            imgs = bs4obj.select('img')[2].get('src')
            image_url = "https://www.pokemon-card.com/"+ imgs
            req = requests.get(image_url)
            path = "../picture_data/" + str(pack)+"/"+str(url_number) + ".jpg"
            with open(path,'wb') as file:
                file.write(req.content)
