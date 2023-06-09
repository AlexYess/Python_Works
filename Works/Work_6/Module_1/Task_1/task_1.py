import math


def deriv(f):
    def approximate_derivative(x, h=0.0001):
        return (f(x + h) - f(x)) / h

    return approximate_derivative


result = deriv(lambda x: x ** 3)(5)
print(result)
result = deriv(lambda x: x ** 2)(2)
# Ожидаемый результат: 4.0001
print(result)
print(result)
result = deriv(lambda x: math.exp(x))(1)
# Ожидаемый результат: 2.718300000000353
print(result)
