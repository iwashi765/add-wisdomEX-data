# add-wisdomEX-data
**wisdomEXに追加するデータを取得するためのプログラム群です(python3.6.9で動作しました)**

## 追加するまでのおおまかな手順(詳細は後ほど)
1. scrapingフォルダ内のdo_scraping.pyを動かしてカードデータをパック毎にまとめて出力する
2. text_dataフォルダ内のmain.pyを動かしてカード1枚毎のデータにして出力する
3. picture_dataフォルダ内のimage_resize.pyを動かしてカードの画像を縮小してリネームする
4. wisdomフォルダ内のmain.pyを動かしてwisdomの形式に合わせて出力する
5. 作成した画像ファイル、テキストファイルをwisdomEX内のフォルダに配置し、wisdomEX内のエキスパンションが書かれたテキストファイルを編集する

## 各手順でやること(詳細)
**1. scrapingフォルダ内のdo_scraping.pyを動かしてカードデータをパック毎にまとめて出力する**
   - トレーナーズウェブサイトの[カード検索](https://www.pokemon-card.com/card-search/)ページを開き、追加するパックの商品名を指定する
   - scrapingフォルダ内のdo_scraping.pyを開き、カード検索ページの最初のカードのid
(カード詳細ページのURL "ww w.pokemon-card.com/card-search/details.php/card/?????/regu/all" の?????の部分の5桁の数字)を
f_minに、最後のカードのidをf_maxに設定する
   - 同ファイルのpackにパックの名称(sm8a,s1Hなど)を設定する
   - パックの名称フォルダがあるか確認する(なかったらdo_scraping.pyでの記述に合わせて作成)
   - $ python3 do_scraping.py > ../text_data/(パック名称のフォルダ)/data.txt の形で実行してdata.txtに出力する
   - 他のパックについても追加する場合はこの部分の始めから繰り返す
   
**2. text_dataフォルダ内のmain.pyを動かしてカード1枚毎のデータにして出力する**
   - divide_data.pyを開き、folder_list内のパック名称を追加するものだけに編集する
   - $ python3 main.py と実行すると、各パック名のフォルダ内に、0.txtのような形のテキストファイルと、(id).txtの形のテキストファイルが生成される
   - 0.txt,1.txt...のファイルができていればテキストデータを加工する準備は完了
   
**3. picture_dataフォルダ内のimage_resize.pyを動かしてカードの画像を縮小してリネームする**
   - image_resize.pyを開き、追加するパック以外をfolder_listからコメントアウトする
   - pictureフォルダとresizeフォルダに、追加するパック名称のフォルダがあるか確認する(なかったら作成)
   - $ python3 image_resize.py と実行すると、resizeフォルダ内の各パック名称フォルダに縮小した画像が出力される
   - resizeフォルダ内のパック名称フォルダ内に縮小した画像がpokemon_10000.jpgの形であれば画像データの準備は完了
   
**4. wisdomフォルダ内のmain.pyを動かしてwisdomの形式に合わせて出力する**
   - main_text_data.pyを開き、追加するパック以外をfolder_listからコメントアウトする
   - $ python3 main.py > pokemon.txt の形で実行して出力する
   - $ nkf -s pokemon.txt > pokemon_text.dat を実行し、shitjis形式でdatファイルに変換する
   - ここまでエラーなしに実行できればテキストデータの準備が完了
   
**5. 作成した画像ファイル、テキストファイルをwisdomEX内のフォルダに配置し、wisdomEX内のエキスパンションが書かれたテキストファイルを編集する**
   - [wisdomEXのインストール、起動準備は各自やっているものとします](http://player2.g1.xrea.com/2p.user.pokemonwiki.net/wisdom/)
   - WisdomEX.exeがあるフォルダ位置を"wisdom"として、wisdom内のimage/pokemonの中に、縮小した画像を全て移します
   - wisdom内のtextにあるpokemon_text.datを、作成したpokemon_text.datと置き換えます
   - wisdom内のexpansionにあるpokemon_expansion.datを開き、次のように書き換えます(パックの名前をこれから変更する場合は手順4のところでwrite_data.pyのpack_listも合わせて変更しましょう)
   
プロモ  
SM「スターターセット伝説」  
SM「ウルトラフォース」  
SM「ウルトラムーン」  
SM「ウルトラサン」  
SM「禁断の光」  
SM「ドラゴンストーム」  
SM「チャンピオンロード」  
SM「裂空のカリスマ」  
SM「迅雷スパーク」  
SM[ブイズスターター]  
SM「フェアリーライズ」  
SM「超爆インパクト」  
SM「ダークオーダー」  
SM「GXウルトラシャイニー」  
SM「タッグボルト」  
SM「ナイトユニゾン」  
SM「フルメタルウォール」  
SM「ダブルブレイズ」  
SM[ジージーエンド]  
SM[スカイレジェンド]  
SM[ミラクルツイン]  
SM[エフィデオスターター]  
SM[リミックスバウト]  
SM[ドリームリーグ]  
SM[名探偵ピカチュウ]  
SM[オルタージェネシス]  
SM[タッグオールスターズ]  
S[スターターセット(5種)]  
S[ソード]  
S[シールド]  
S[ザシアン+ザマゼンタBOX]  
S[VMAXライジング]  
S[反逆クラッシュ]  
S[スターターリザードン,オーロンゲ]  
S[爆炎ウォーカー]  
S[ムゲンゾーン]  

## これでwisdomEX内の編集は完了で、データ追加のための作業も完了です。

ここまでやってDeckEditorPM.exeを起動するとカードが追加されており、右クリックで対応した画像も表示されます。
申し訳ありませんがpython実行時のエラーは逐一対応できないため、エラーメッセージの内容を見て適宜修正してください。
