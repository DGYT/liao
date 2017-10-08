def a():
    global h
    h = {'a': 1, 'b': 2}


def b():
    global h
    h = {}
    arg = h.get('a')
    print(arg)


a()
b()
