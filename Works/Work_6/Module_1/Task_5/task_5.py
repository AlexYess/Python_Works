def collect(cls):
    cls._objects = []

    # Create a wrapper function to replace the original __init__ method
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls._objects.append(self)

    cls.__init__ = new_init

    def get_objects():
        return cls._objects

    cls.get_objects = staticmethod(get_objects)

    return cls


@collect
class C1:
    pass


a = C1()
b = C1()
c = C1()

print(C1.get_objects())
