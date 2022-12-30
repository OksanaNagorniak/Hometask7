# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла
# (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
N = int(input("Введите количество чисел в списке А: "))
A = []
for i in range(N):
    v = int(input("Введите число для списка: "))
    A.append(v)
print(A)
Amax = A[0]
Amin = A[0]
for i in range(N):
    if A[i] > Amax:
        Amax = A[i]
    if A[i] < Amin:
        Amin=A[i]
print ('Max:', Amax, 'MIn:', Amin)
