def binary_search(array, element, left, right):
    middle = (right + left) // 2  # находим середину
    if left > right:  # если левая граница превысила правую,
        return middle  # значит элемент отсутствует
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

def sortirovka(array): #функция сортировки вставками
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

array = input('Введите последовательность через пробел = ')  # вводим последовательность
array = list(map(int, array.split())) #преобразовываем в список
sortirovka(array) #сортируем последовательность
print(array)

element = int(input('Введите число для поиска = '))

if element<array[0] or element>array[len(array)-1]: #если не входит в диапазон
    print('Введенное число вне диапазона последовательности') #выводим ошибку
else:
    print('Позиция = ', binary_search(array, element, 0, len(array)-1)) #ищем позицию числа в последовательности


