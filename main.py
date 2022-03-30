# Комментарии к оформлению:
# Пока что пишем модулями(т.е. каждый назывет модуль типа ИМЯФ.py и подключает сюда (название на инглише, прим SEVAB.py)
# В модуле ваши функции, которые вызываются через точку типа(по сути просто пишите ваши функции в :
# import SEVAB
# SEVAB.funct_name()

# Адекватно называем переменные(кроме счётчиков циклов)
# Юзаем как можно больше комментариев (чтобы было понятно, че вы там написали)
# Между логическими частями ставьте пробелы, чтобы красиво (особенно перед комментариями)
# Ну и оставшиеся правила:
# Читы - бан
# Стельба по своим - бан
# Оскорбление администрации - расстрел, а потом бан.

from Naturals import MUL_ND_N
from Dtypes import RNumber, NNumber, Integer, Polynomial
# показываю пример работы с типами
rnum = RNumber(Integer('-0'), NNumber([1,2,3]))
# Я реализовал удобный вывод, так чтобы вы не парились
print(rnum)  # 0
# можно задать строкой!
rnum = RNumber('-123/55')
print(rnum)  # -123/55

# Натуральное задаётся просто массивом цифр
# Конструктор принимает в интуитивном порядке 123 = 1,2,3
nnum = NNumber('000000123')
# Но представляется в обратном
print(nnum.get_num())  # 3 2 1
# Вывод тоже удобный
print(nnum)  # 123


# Целое списком и знаком
# True = отрицательное
# False = положительное
inum = Integer('-123')
# Представление тоже обратное
print(inum.get_num())  # 3 2 1
# Вывод комфортабельный
print(inum)  # -123


# Многочлен - список из элементов типа Rnumber
rli = [RNumber(Integer('0'),NNumber('100'))]+[RNumber(Integer([i]), NNumber([2+i])) for i in range(4)]  # дробь 0 задаётся видом 0/1
print([i.__str__() for i in rli])  # сам список
pol = Polynomial(rli)
# Представление тоже обратное
print([i.__str__() for i in pol.get_coefs()])  # ['3/5', '2/4', '1/3', '0']
# Вывод тож реализовал
# где коэф 0 - не выводится
print(pol)  # (3/5)x^3 (2/4)x^2 (1/3)x^1
# Ура, можно теперь задать строкой!!!
st = '0 0 0 123/166 0 123/123 -1999/1'
pol = Polynomial(st)
print(pol) # (123/166)x^3 + (123/123)x^1 - 1999

inst = Integer([6,0,0,0,0,0],False)
inst_r = MUL_ND_N(inst,2)
print("\n\n\n\n")
print(inst_r.get_num())