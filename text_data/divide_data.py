import output_data

folder_list = {
    'PROMO','sm5S','sm5M','sm5+','sm6','sm6a','sm6b','sm7','sm7a','sm7b','sm8','sm8a','sm8b','smE',
    'sm9','sm9a','sm9b','sm10','sm10a','sm10b','sm11','sm11a','sm11b','sm12','sm12a','smI','smM',
    's1H','s1W','s1a','s2','s2a','sA','sC','smP2','sp1'
}

#タイプを漢字に置き換え
def type_replace(data):
    data = data.replace('icon-none','無色')
    data = data.replace('icon-fire','炎')
    data = data.replace('icon-water','水')
    data = data.replace('icon-grass','草')
    data = data.replace('icon-electric','雷')
    data = data.replace('icon-fighting','闘')
    data = data.replace('icon-psychic','超')
    data = data.replace('icon-dark','悪')
    data = data.replace('icon-steel','鋼')
    data = data.replace('icon-fairy','妖')
    data = data.replace('icon-dragon','龍')
    data = data.replace('icon-void','--')
    data = data.replace('icon-plus','+')
    return data

#1行ずつタイプの記述があるか判定
def type_judge(data):
    for row in range(0,len(data)):
        data[row] = type_replace(data[row])
    return data

#data.txtからカード毎に分けて出力
def divideData(data,number,pack):
    data_start = 0
    for page in range(number):
        write_path = str(pack) + '/' + str(page) + '.txt'
        with open(write_path,mode='w') as w:
            for row in range(data_start,len(data)):
                if data[row] == '/':
                    data_start = row + 1
                    break
                w.write(data[row]+'\n')
        
#カードごとのデータを読み込めるように整える
def typeshift(data,number,pack):
    for file_number in range(number):
        path = str(pack) + '/' + str(file_number) + '.txt'
        with open(path,mode='r') as r:
            data = r.readlines()
            data[1] = data[1].replace(' ','')
            data[len(data)-2] = data[len(data)-2].replace('\n','')
            data = type_judge(data)
            for row in range(len(data)):
                data[row] = data[row].replace(' ','\n')
            write_path = str(pack) + '/' + str(file_number) + '.txt'
            with open(write_path,mode='w') as w:
                for row in range(0,len(data)):
                    if row == len(data)-2:
                        w.write(data[row] + '\n')
                    else:
                        w.write(data[row])

#取り除けなかった空欄があるため調整
def data_adjust(card_number,pack):
    for file_number in range(card_number):
        path = str(pack) + '/' + str(file_number) + '.txt'
        with open(path,mode='r') as r:
            data = r.read().splitlines()
            output_data = list(range(len(data)+2))
            data_row = 0
            for row in range(len(data)):
                output_data[data_row] = data[row]
                if row != len(data)-1:
                    if data[row] == data[row+1] and data[row] == '':
                        output_data[data_row] = 0
                data_row = data_row + 1
            write_path = str(pack) + '/' + str(file_number) + '.txt'
            with open(write_path,mode='w') as w:
                for row in range(len(output_data)):
                    if row != output_data[row] and output_data[row] != '' :
                        w.write(str(output_data[row]) + '\n')

#カードの種類毎に処理する関数を変える
def data_send(card_number,pack):
    for file_number in range(card_number):
        path = str(pack) + '/' + str(file_number) + '.txt'
        with open(path,mode='r') as r:
            data = r.read().splitlines()
            title = data[0]
            if title == 'ポケモン':
                output_data.pokemon_output(data,pack)
            elif title == 'グッズ':
                output_data.traner_output(data,pack)
            elif title == 'ポケモンのどうぐ':
                output_data.traner_output(data,pack)
            elif title == 'サポート':
                output_data.traner_output(data,pack)
            elif title == 'スタジアム':
                output_data.traner_output(data,pack)
            elif title == '特殊エネルギー':
                output_data.energy_output(data,pack)
            elif title == '基本エネルギー':
                output_data.basic_energy_output(data,pack)

def divide():
    for pack in folder_list:
        inputfile = str(pack) + '/data.txt'
        with open(inputfile,mode='r') as f:
            data = f.read().splitlines()
            for row in range(len(data)):
                data[row] = data[row].replace('\xa0','')
            card_number = data.count('/')
            print(pack)

#各関数で順番に処理
            divideData(data,card_number,pack)
            typeshift(data,card_number,pack)
            data_adjust(card_number,pack)
            data_send(card_number,pack)

def order():
    for pack in folder_list:
        inputfile = str(pack) + '/data.txt'
        with open(inputfile,mode='r') as f:
            data = f.read().splitlines()
            card_number = data.count('/')
            typeshift(data,card_number,pack)

############################### main の部分 ##################################################
