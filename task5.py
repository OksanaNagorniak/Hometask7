
# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

A = []
for i in range(5):
    v = int(input('Введите число: '))
    A.append(v)
print(A)
C = [A[i] for i in range(len(A)) if int(A[i]) > 5]
print(C)
