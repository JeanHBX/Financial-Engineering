作業四：


根據Black-Scholes Model來計算EU put 和call option的value.
這份作業比較前幾份作業直觀，就是一步一步來


先算出option的dividend本利和以及其折現
要派幾次利息，很無腦地用if elif來寫：


一次就1個月；


兩次就1個月和4個月；


三次就1個月，4個月，7個月；


四次就1個月，4個月，7個月和10個月；

dividend = pay_div_amt*e**(risk_free_rate*(-1/12)) + pay_div_amt*e**(risk_free_rate*(-4/12)) + pay_div_amt*e**(risk_free_rate*(-7/12)) + pay_div_amt*e**(risk_free_rate*(-10/12))


接著就是要估計stock price，

根據公式 estimated stock price = stock price - dividend（分股利會使股票價值下滑）
搞定這些配料後，就要開始BSM的主食：d1, d2


公式：


d1 = (np.log(estimated_stock_price/exercise_price) + (risk_free_rate + 0.5*sigma**2)*(maturity_yr/12))/(sigma*((maturity_yr/12)**(1/2)))


d2 = d1 - sigma*((maturity_yr/12)**(1/2))


之後再用BSM和put call parity公式，計算put value和call value
https://wikimedia.org/api/rest_v1/media/math/render/svg/d1f576effba2c7cabdebb78ac63fbb75b850a714


比較有問題是在操作stats.norm.cdf 的時候


按道理normal distribution應該是直接用上面那個function來算cdf（參考老師week 7 slide pg 30）


但我計算的時候卻沒辦法得到test value的答案（參考老師week 7 slide pg 40），於是嘗試了其他如pdf等後，靈機一動試試 (1-stats.norm.cdf)
結果N(-d1), N(-d2)值就剛好和test value上面一樣了？
我猜是因為 1- N(d1) = N(-d1) = stats.norm.cdf 的關係

（我真的很弱  連stats套件都查了半天才勉強能用

大概就是這樣，請多見諒，謝謝
