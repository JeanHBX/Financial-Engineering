import math 

bond_price = int(input("bond_price:")) #PV
bond_par_value = int(input("bond_par_value:")) #F
coupon_rate = int(input("coupon_rate(%):")) #c
years_to_maturity = int(input("years_to_maturity:")) #n
payment_per_year = int(input("payment_per_year:")) #m

annual_coupon_rate = coupon_rate/100 #r
total_num_payment = payment_per_year*years_to_maturity #num =mn
coupon = bond_par_value*annual_coupon_rate/payment_per_year #C=Fc/m
payment_rate = annual_coupon_rate/payment_per_year #r/m

#annual payment的ytm
ytm = (coupon + (bond_par_value - bond_price)/years_to_maturity)/((bond_par_value + bond_price)/2)
print("ytm is:",ytm)

i = 1
spot_rate_list = []
forward_rate_list = []

while i in range(1,total_num_payment+1):
    spot_rate = (1+ytm)**i -1 #coupon的PV = coupon/(1+ytm)**t = coupon*spot_rate
    print("time",i,"spot_rate is:",spot_rate)
    spot_rate_list.append(spot_rate)
    i += 1 

print(spot_rate_list)

i = 0
j = 1 
#forward_rate = (((1+ x**j)/(1+ y**i))**(1/(j-i)))-1  
    
while j in range(1,total_num_payment):
    x = spot_rate_list[j] #比較遠的j
    y = spot_rate_list[i] #比較近的i
    forward_rate = ((1+x)**j)/((1+y)**i) -1
    print("at time",i,"forward_rate to",j,forward_rate)
    forward_rate_list.append(forward_rate)
    i += 1
    j += 1

print(forward_rate_list)