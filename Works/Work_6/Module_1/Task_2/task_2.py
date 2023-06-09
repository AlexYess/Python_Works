def person(**kwargs):
    def get(key):
        return kwargs.get(key)

    def replace(key, value):
        new_kwargs = {**kwargs, key: value}
        return person(**new_kwargs)

    return {
        'get': get,
        'replace': replace
    }


p1 = person(name='Иван', age=20)
p2 = p1['replace']('name', 'Алексей')['replace']('age', 21)

print(p1['get']('name'), p1['get']('age'))  # ('Иван', 20)
print(p2['get']('name'), p2['get']('age'))  # ('Алексей', 21)
