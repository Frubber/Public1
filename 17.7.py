#имеем словарь с процентными ставками
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#вводим сумму вклада, преобразуем в число, выводим на экран
money =  int(input("Введите сумму вклада:"))
print("money =", money)

#создаем список процентов deposit значений из словаря per_cent, умножаем на сумму вклада, выводим на экран
deposit = list(per_cent.values())
deposit = [money*deposit[0]/100, deposit[1]*money/100, deposit[2]*money/100, deposit[3]*money/100]
print("deposit =", deposit)
#выводим на экран максимальное значение
print("Максимальная сумма, которую вы можете заработать", max(deposit))

#выводим на экран округленные целые значения списка
print("deposit =", list(map(int, deposit)))
