HW5 Option Pricing with Hull White Model

透過 Monte Carlo method
對 Hull White Model 模擬 Short Rate
將 Short Rate 帶入 Geometric Brownian Motion，r 換成 r(t) 模擬股價
自訂選擇權履約價，對每一條 path 計算出到期日時的 PayOff
對所有 Path 的 PayOff 進行期望值計算，並折現回 t=0 的時間點
計算出 Call Price & Put Price

首先，先學習如何直接使用QL套件，我參考了以下網址：
http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html



設定好讓人輸入的Interest rate的相關資訊，接著就使用QL套件來跑Hull White，最後會產生一段時間內的[利率]和走勢圖





接著呢，參考老師的Geometric Brownian Motion寫法（以下網址）來做：
https://colab.research.google.com/drive/1LL_m1UO_U2oHDMQhBDPjhUBANDpVhev7#scrollTo=nM_mFTMxlLWa




一樣，先設定好讓人輸入的stock price的相關資訊，記得用我們上面的模擬r來替代GBM裡面本來的r

。
通過Monte carlo stimulation計算未來資產價格，再取期望值、折現回來得到call, put的price
