class raises:
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            raise AssertionError(f"Expected {self.expected_exception}, but no exception was raised.")
        if not issubclass(exc_type, self.expected_exception):
            raise AssertionError(f"Expected {self.expected_exception}, but got {exc_type.__name__}.")
        return True


class MealyError(Exception):
    pass


# Пример использования менеджера контекста raises
try:
    with raises(MealyError) as e:
        raise MealyError("This is a custom error")
except AssertionError as e:
    print(e)
