import math

p = int(input())
y = int(input())
r = int(input())

prin = p*10000
no_pay = y*12
annual_rate = r/100
coupon = prin/no_pay

i = 1
while i in range(1,no_pay+1):
    print("month",i)
    print("coupon monthly",round(coupon))
    int_pay = prin*annual_rate/12
    print("interest paid",round(int_pay))
    if i == 1:
        total_paid = (i*coupon+ int_pay)
        print("total paid",total_paid)
        i += 1
        prin -= coupon
    else:
        prin -= coupon
        #print("principal left",prin)
        int_pay = int_pay + last_int_pay
        total_paid = (i*coupon + int_pay)
        print("accumulated total paid",round(total_paid))
        i += 1
    last_int_pay = int_pay
    print(" ")