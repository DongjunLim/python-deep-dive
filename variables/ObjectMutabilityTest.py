

if __name__ == '__main__':
    list1 = [1, 2, 3]

    print(hex(id(list1)))

    list1.append(4)

    print(hex(id(list1)))

    a = "hello"
    b = a

    print(hex(id(a)))
    print(hex(id(b)))

    b = b + " world"

    print(hex(id(b)))
    assert 1 == 2, "둘이 다릅니다"
