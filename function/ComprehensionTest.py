def fact(n):
    return 1 if n < 2 else n*fact(n-1)


if __name__ == '__main__':
    l = [10, 20, 30, 40, 50]
    print([fact(x) for x in range(1, 10)])
    print([fact(x) for x in range(1, 10) if x < 6])
    print([x+y for x, y in zip(l, range(10)) if (x + y) % 2 == 0])