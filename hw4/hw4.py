import math
import numpy as np
from scipy import stats

stock_price = int(input("stock price:",)) #75
sigma = float(input("sigma in decimal:",)) #0.35
pay_div_num_per_year = int(input("pay dividend how many times:",)) #2
pay_div_amt = int(input("pay dividend amount:",)) #1
risk_free_rate = float(input("risk free rate in decimal:",)) #0.06
exercise_price = int(input("exercise price:",)) #65
maturity_yr = int(input("maturity in how many months:",)) #6
dividend = 1
e = 2.7182

#count dividend
if pay_div_num_per_year == 1:
    dividend = pay_div_amt*e**(risk_free_rate*(-1/12))
    print("dividend :",dividend)
elif pay_div_num_per_year == 2:
    dividend = pay_div_amt*e**(risk_free_rate*(-1/12)) + pay_div_amt*e**(risk_free_rate*(-4/12))
    print("dividend :",dividend)
elif pay_div_num_per_year == 3:
    dividend = pay_div_amt*e**(risk_free_rate*(-1/12)) + pay_div_amt*e**(risk_free_rate*(-4/12)) + pay_div_amt*e**(risk_free_rate*(-7/12))
    print("dividend :",dividend)
elif pay_div_num_per_year == 4:
    dividend = pay_div_amt*e**(risk_free_rate*(-1/12)) + pay_div_amt*e**(risk_free_rate*(-4/12)) + pay_div_amt*e**(risk_free_rate*(-7/12)) + pay_div_amt*e**(risk_free_rate*(-10/12))
else:
    print("out of range")

#estimate stock price
estimated_stock_price = stock_price - dividend
print("estimated stock price: ",estimated_stock_price)

#d1,d2
d1 = (np.log(estimated_stock_price/exercise_price) + (risk_free_rate + 0.5*sigma**2)*(maturity_yr/12))/(sigma*((maturity_yr/12)**(1/2)))
d2 = d1 - sigma*((maturity_yr/12)**(1/2))
print("d1:",d1,"d2:",d2)


#put and call value, using put-call parity
call = estimated_stock_price * (1-stats.norm.cdf(d1,0.0,1.0)) - exercise_price * e**(-risk_free_rate*(maturity_yr/12)) * (1-stats.norm.cdf(d2,0.0,1.0))
put = exercise_price *e**(-risk_free_rate*(maturity_yr/12)) * (1-stats.norm.cdf(d2,0.0,1.0)) - estimated_stock_price * (1-stats.norm.cdf(d1,0.0,1.0))
print("put value :",put)
print("call value :",call)
