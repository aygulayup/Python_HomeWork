# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример: *

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

#a = int(input('Введите трехзначное число: '))
#sum = a//100 + a%10 + a//10%10
#print(sum)



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# *Пример: *

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# sum = int(input('введите общее количество журавликов кратное 6: '))
# if sum % 6 != 0:
#     print('Введите корректную сумму')
# else:
#     petya = sum//6
#     katya = sum * 2//3
#     sergey = sum//6
#     print(f'{sum} -> {petya} {katya} {sergey}')



# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – 
# счастливый, т.к. 3+8+5 = 9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.
# *Пример: *

# 385916 -> yes
# 123456 -> no

# num = str(input('введите шестизначный номер: '))
# sum1 = int(num[0]) + int(num[1]) + int(num[2])
# sum2 = int(num[3]) + int(num[4]) + int(num[5])
# if (sum1 == sum2):
#     print('-> yes')
# else:
#     print('-> no')



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками(то есть разломить шоколадку на два прямоугольника).
# *Пример: *

# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('введите дольки длины шоколада: '))
n = int(input('введите дольки ширины шоколада: '))
k = int(input('количество отламываемых долек: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')