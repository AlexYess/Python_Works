factorial = (lambda f: (lambda x: x(x))(lambda y: f(lambda x: y(y)(x))))(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))

result = factorial(5)
result2 = factorial(3)
print(result, result2)
