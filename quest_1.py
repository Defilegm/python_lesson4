# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141.   10^(-1) ≤ d ≤10^(-10)



import math


print(math.pi)

def f(d,n):   # d - кол-во знаков после запятой, n - входное число
    num = (n - int(n))*(10**d)
    if num*10%10>=5:
        num+=1
    return int(n)+int(num)/(10**d)
print(f(12,math.pi))

    
