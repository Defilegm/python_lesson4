# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


def f(n,lst=[]):
    count = 2
    countnum = 0
    if n > 1:
        while(n%count !=0 ):
            count+=1
        while n%count == 0:
            n /= count
            countnum+=1
        if countnum>1:
            lst.append(f'{count}^{countnum}')
        else:
            lst.append(f'{count}')
        print(lst)
        return f(n,lst)
    return lst

print(f(154))
