作業三：製作binomial tree

看到那一大段的code就知道在下的code功薄弱 @@
我先依據老師week5投影片第44，45頁來構思，思考每一期stock price該怎麼寫
想到binomial tree分支結果一定比 no. of periods 多1個數字，且u和d的指數加總必定等於no. of periods
因此用兩個for 搭配，加上把Su = uS0,Sd = dS0公式化，跑出每期的stock price後存在list裡面

接著就要構思call/put price
根據backward induction，由最後一組stock price下手，跟strike price相減，得到最後一組call/put value
然後再依據公式，Cu = (p*Cuu + (1-p)*Cud)/R 來計算每期的call/put value，存到list

無奈一直卡在無法將list內容取出轉換成matrix形式
這點會在作業截止後多多觀摩大家是怎麼辦到的> <
