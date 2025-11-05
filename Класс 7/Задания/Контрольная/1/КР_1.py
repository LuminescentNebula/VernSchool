distance = float(input("Введите расстояние, км:\n"))
tarif = float(input("Введите тариф за 1 км:\n"))
time = int(input("Введите время (1 - день, 2 - ночь):\n"))
money = float(input("Введите ваш бюджет:\n"))


if time==2:
    print("Ночной тариф: +20%")
    tarif=tarif*1.2
final = distance*tarif
if distance>20:
    final=final*0.95
    print("Итоговая сумма со скидкой 5%:",final)
else:
    print("Итоговая сумма:",final)
average = final/distance
print("Средняя стоимость за 1 км:",'{:.2f}'.format(average))
if final>money:
    print("Бюджета не хватает! Необходимо еще", '{:.2f}'.format(final-money))
else:
    print("Бюджета хватает!")
    

