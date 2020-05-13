HW5 Option Pricing with Hull White Model

首先，先學習如何直接使用QL套件，要如何在windows上python安裝QL，這個費了我一陣子的時間/.\
然後我參考了以下網址來運用：
http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html



設定好讓人輸入的Interest rate的相關資訊，接著就使用QL套件來跑Hull White，最後會產生一段時間內的[利率]和走勢圖





接著呢，參考老師的Geometric Brownian Motion寫法（以下網址）來做：
https://colab.research.google.com/drive/1LL_m1UO_U2oHDMQhBDPjhUBANDpVhev7#scrollTo=nM_mFTMxlLWa




一樣，先設定好讓人輸入的stock price的相關資訊，記得用我們上面的模擬r來替代GBM裡面本來的r

。
通過Monte carlo stimulation計算未來資產價格，再取期望值、折現回來得到call, put的price
