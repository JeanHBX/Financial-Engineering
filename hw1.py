import math

p = int(input()) #輸入本金（萬）
y = int(input()) #輸入年份
r = int(input()) #輸入年利率（%）

prin = p*10000
no_pay = y*12
annual_rate = r/100
coupon = prin/no_pay #每期固定還的本金

i = 1
while i in range(1,no_pay+1):
    print("month",i)                      #第幾期
    print("coupon monthly",round(coupon)) #還的本金（固定）
    int_pay = prin*annual_rate/12         #還欠的金額（變動）×月利率
    print("interest paid",round(int_pay)) #本期要還的利息
    if i == 1:
        total_paid = (i*coupon+ int_pay)  #第一期要還的金額
        print("total paid",total_paid)
        i += 1
        prin -= coupon
    else:
        prin -= coupon                    #更新還欠的金額
        #print("principal left",prin)
        int_pay = int_pay + last_int_pay  #更新已還利息
        total_paid = (i*coupon + int_pay) #更新總共還的金額
        print("accumulated total paid",round(total_paid))
        i += 1
    last_int_pay = int_pay                #記得上一期還的利息
    print(" ")
