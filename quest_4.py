# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import math,random
k = int(input('Введите натуральную степень k: '))



w = random.randint(0,100)

f = lambda num ,k,a = str(f'{random.randint(0,100)}*x^{k}'): f'{random.randint(0,100)}*x'+f'+{random.randint(0,100)}' if k==1 else a + '+'+ f(random.randint(0,100),k-1, f'{random.randint(0,100)}*x^{k-1}')
print(f(random.randint(0,100),k))
o = open('mnogochlen1.txt','w')
o.write(f(random.randint(0,100),k))
o.close
otwo = open('mnogochlen2.txt','w')
otwo.write(f(random.randint(0,100),k,a = str(f'{random.randint(0,100)}*x^{k}')))
otwo.close





