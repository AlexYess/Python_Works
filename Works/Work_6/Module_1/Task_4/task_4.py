def io(*args):
    def decorator(func):
        def wrapper():
            inputs = [arg() for arg in args[:func.__code__.co_argcount]]
            result = func(*inputs)
            print(result)

        return wrapper

    return decorator


@io(lambda: input("Enter x: "), lambda: input("Enter y: "), lambda: input("Enter z: "), print)
def f1(x, y, z):
    return x + y + z


f1()
