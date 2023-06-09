def remaining_days(workers, days, name):
    num = -1
    for i in range(len(workers)):
        if workers[i] == name:
            num = i
    if num == -1:
        return 0
    else:
        return 30 - days[num]


print(remaining_days(['Г', 'С', 'Л', 'Са', 'К'], [24, 21, 23, 22, 21], 'К'))
print(remaining_days(['Саша', 'Сережа', 'Катя', 'Валера', 'Богдан'], [30, 30, 29, 30, 26], 'Сережа'))
print(remaining_days(['Оля', 'Миша', 'Юра', 'Богдан', 'Богдан'], [30, 30, 29, 30, 26], 'Богдан'))