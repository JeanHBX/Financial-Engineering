#put binomial tree
import math
import numpy as np

S0 = int(input("S0 = ",))
N = int(input("N = ",))
u = float(input("u = ",))
d = float(input("d = ",))
r = float(input("r = ",))
X = int(input("X = ",))
p = int(input("p =",))
R = 2.71828**r

#count stock price of every period, save in list a
a = []
for i in range(N + 1): 
    #print("N =",i) 
    list = []
    for j in range(i + 1):
        stock = (d ** (i - j)) * (u ** j) * S0 
        list.append(stock)
        #print(stock)
    print("stock price in period",i,list)
    a.append(list)
print("stock price every period:",a)


#select the last period stock price,  put value of last period = max(0, X-S0)
put_value = []
for i in range(N + 1):
    put = max(0, X-a[N][i])
    put_value.append(put)
    #print(put)
print("put value of last period:",put_value)


#using formula, backward induction to get put price of previous period
M = N
value = []
value.append(put_value)
for i in range(N):
    prev_option = []
    for j in range(M):
        #print(i,j)
        option = ((1-p)*put_value[j] + (p)*put_value[j+1])/R
        prev_option.append(option)
        #print(prev_option)
    M -= 1
    put_value = prev_option
    print("put value in period",N-i-1,put_value)
    value.append(put_value)
print("put value in every(backward) period:",value)
