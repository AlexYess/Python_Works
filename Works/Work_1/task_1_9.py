x = 5
print(1 < x < 10)  # здесь сравнивается переменная x ,в данном случае будет True
x = 5
print(1 < (x < 10))  # здесь сначала в порядке приоритета (из-за скобок) проверяется выражение (x < 10)
# и получается значение True, а дальше идёт проверка выражения  (1 < True), а так как PY язык с
# динамической типизацией данных, то True становится 1 и в таком случае результат выражения равен
# False

