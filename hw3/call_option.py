#call binomial tree
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
        stock = (u ** (i - j)) * (d ** j) * S0 
        list.append(stock)
        #print(stock)
    print("stock price in period",i,list)
    a.append(list)
print("stock price every period:",a)


#select the last period stock price,  call value of last period = max(0, S0-X)
call_value = []
for i in range(N + 1):
    call = max(0, a[N][i]-X)
    call_value.append(call)
    #print(call)
print("call value of last period:",call_value)


#using formula, backward induction to get call price of previous period
M = N
value = []
value.append(call_value)
for i in range(N):
    prev_option = []
    for j in range(M):
        #print(i,j)
        option = (p*call_value[j] + (1-p)*call_value[j+1])/1.2
        prev_option.append(option)
        #print(prev_option)
    M -= 1
    call_value = prev_option
    print("call value in period",N-i-1,call_value)
    value.append(call_value)
print("call value in every(backward) period:",value)


#call_array = np.array(value)
#print(call_array)
#call_matrix = np.asmatrix(call_array)
#print(call_matrix)
