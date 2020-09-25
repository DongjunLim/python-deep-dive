from collections import deque
if __name__ == '__main__':
    a = 10
    b = 10
    print(hex(id(a)))
    print(hex(id(a)))


    print("a is b", a is b)
    print("a == b", a == b)

    a = 25500000000
    b = 25500000000

    print(hex(id(a)))
    print(hex(id(a)))

    print("a is b", a is b)
    print("a == b", a == b)

    a = [1, 2 + 1, 3]
    b = [1, 2, 3]
    c = map(int, b)
    print(hex(id(a)))
    print(hex(id(a)))

    print("a is b", a is b)
    print("a == b", a == b)

    a = 10
    b = 10.0

    print(hex(id(a)))
    print(hex(id(a)))

    print("a is b", a is b)
    print("a == b", a == b)

    l = [1, 2, 3, 4, 5]

    print(list(zip(l, range(len(l)))))