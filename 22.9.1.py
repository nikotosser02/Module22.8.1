
# # --------------------------Сортировка слиянием, взята полностью с учебного блока, так как и так работает :)
#
def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Бинарный поиск реализован без рекурсии (рекурсия, как понимаю, больше по времени выполняется)
def binary_search(array, elem):

    first = 0
    last = len(array)-1
    # print("array[first]: ", array[first]," array[last]: ",array[last])
    if elem > array[last] or elem < array[first]: #проверка введенного любого числа на вхождение диапазон
        return -1
    index = -1


    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if array[mid] == elem or (array[mid] < elem and array[mid+1] >= elem): #проверка условия 3 из задачи
            index = mid
        else:
            if elem < array[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

# Ввод данных реализован через функции

def vvod_posled():

    while True: #Запрашиваем последовательность чисел через пробел и проверяем, что это числа. Одновременно преобразование в список.
        try:
            spisok_chisel = list(map(int, input("Введите последовательность чисел через пробел: ", ).split()))
            break
        except ValueError as error:
            print("Нужно вводить только числа !!!")
        continue
    return spisok_chisel

def vvod_l_chisla():
    while True: #Запрашиваем у пользователя любое число и проверяем. что оно число
        try:
            element = int(input("Введите любое число: ", ))
            break
        except ValueError as error:
            print("Нужно вводить только число !!!")
        continue
    return element

spisok_chisel = vvod_posled()
element = vvod_l_chisla()

# выход за переделы пример
# spisok_chisel = [3, 5, 6, 2, 76, 23, -23, 33, 3]
# element = -30

# # нормальный пример
# spisok_chisel = [3, 5, 2, 6, 2, 4, 3, 3]
# element = 4

print("\n\n\n\nИсходный список: ", spisok_chisel)
print("Ваше число: ",element)
sortirovanniy_spisok = merge_sort(spisok_chisel)
print("Сортированный список: ", sortirovanniy_spisok)
# запускаем алгоритм на левой и правой границе

index = binary_search(sortirovanniy_spisok, element)

if index == -1:
    print("Ваше число ", element, " выходит за рамки диапазона")
else:
    print("Индекс в списке: ", index, ", где входит введенное число ", element, " \nПо условию: ",
          sortirovanniy_spisok[index], " < ", element, " <= ", sortirovanniy_spisok[index + 1])
input("Нажмите любую клавишу для закрытия")