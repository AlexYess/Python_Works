class MealyError(Exception):
    pass


class Mealy:
    def __init__(self):
        self.st = "A"

    def paste(self):
        if self.st == "A":
            self.st = "B"
            return 0
        else:
            raise MealyError("paste")

    def scan(self):
        if self.st == "B":
            self.st = "C"
            return 1
        elif self.st == "C":
            self.st = "D"
            return 3
        elif self.st == "E":
            self.st = "F"
            return 4
        else:
            raise MealyError("scan")

    def start(self):
        if self.st == "C":
            self.st = "D"
            return 2
        elif self.st == "F":
            self.st = "G"
            return 8
        elif self.st == "A":
            self.st = "B"
            return 9
        else:
            raise MealyError("start")

    def swap(self):
        if self.st == "D":
            self.st = "E"
            return 7
        elif self.st == "F":
            self.st = "A"
            return 9
        else:
            raise MealyError("swap")


def main():
    return Mealy()


def test():
    o = main()
    assert o.paste() == 0
    assert o.scan() == 1
    assert o.scan() == 3
    assert o.start() == 6
    assert o.scan() == 9
    assert o.start() == 2
    assert o.start() == 11
    raises(lambda: o.swap(), MealyError)
    assert o.scan() == 3
    assert o.swap() == 4
    assert o.swap() == 7
    assert o.paste() == 8
    assert o.paste() == 10
    assert o.start() == 11
    raises(lambda: o.paste(), MealyError)
    assert o.scan() == 3
    assert o.paste() == 0
    o = main()
    assert o.paste() == 0
    assert o.scan() == 1
    assert o.scan() == 3
    assert o.swap() == 4
    assert o.swap() == 7
    raises(lambda: o.start(), MealyError)
    assert o.scan() == 9
    raises(lambda: o.swap(), MealyError)
    assert o.start() == 2
    assert o.start() == 11
    assert o.scan() == 3
    raises(lambda: o.paste(), MealyError)
    assert o.start() == 6
    assert o.paste() == 8
    assert o.paste() == 10
    assert o.start() == 11
    assert o.scan() == 3
    assert o.scan() == 5


def raises(func, error):
    try:
        func()
    except Exception as e:
        assert isinstance(e, error)


test()
