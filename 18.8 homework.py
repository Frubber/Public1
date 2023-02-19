# Заправшиваем количество билетов
N_tickets = int(input("Введите количество билетов, которое хотите приобрести = "))
print("ввели кол-во", N_tickets)

# Запрашиваем возраст посетителя
age = [int(input("Введите возраст посетителя = ")) for i in range(N_tickets)]
#Считаем общую сумму в соответствии с условиями
total_price=0
for i in age:
    if 0<= i < 18: #менее 18 лет, то он проходит на конференцию бесплатно
        total_price = total_price+0
    elif 18<= i <= 25: # От 18 до 25 лет — 990 руб.
        total_price = total_price+990
    elif 26<= i: # От 25 лет — полная стоимость 1390 руб.
        total_price = total_price + 1390
print("Полная стоимость билетов = ", total_price)
# Проверяем условие, если человек зарегистрировал больше трёх человек на конференцию, то применяем скидку 10%
if 3 < N_tickets:
    total_price = total_price - 0.1 * total_price
    print("Сумма к оплате c учетом скидки 10% = ", int(total_price))
else:
    print("Cумма к оплате = ", total_price)





