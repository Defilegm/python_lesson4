# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

f = open('mnogochlen1.txt').read()
a = open('mnogochlen2.txt').read()


def summ(x):
    lst=[]
    count =''
    i=0
    while i < len(x):
        while i < len(x) and x[i] != '*' and x[i] != '+':
            count+=x[i]
            i+=1 
        i+=1
        lst.append(count)
        count = ''
    return lst
print(summ(f))
print(summ(a))
lst =[]
print(summ(f)[1].isdigit())

for i in range(len(summ(f))):
    if summ(f)[i].isdigit() == False:
        for j in range(len(summ(a))):
            if summ(f)[i]==summ(a)[j]:
                lst.append(int(summ(f)[i-1])+int(summ(a)[j-1]))
                lst.append(summ(f)[j])


lst.append(int(summ(f)[-1])+int(summ(a)[-1]))
print(lst)
resultstr =''
for i in range(len(lst)):
    if str(lst[i]).isdigit() and i<len(lst)-1:
        resultstr += str(lst[i])+'*'+str(lst[i+1])
    elif str(lst[i]).isdigit() == False and i<len(lst)-1 and i != len(lst)-1:
        resultstr += '+'
resultstr+=str(lst[-1])

print(resultstr)
        

o = open('resultmnogochlen.txt','w')
o.write(resultstr)
o.close






        
    



