import sys
import time


def calc(a):
    for i in range(10000000):
        a * 2


if __name__ == '__main__':

    print(sys.getsizeof(True))
    print(sys.getsizeof(0))

    a = int("11011", 2)
    b = bool(1)
    print(a)
    print(not '')

    # start = time.perf_counter()
    # calc(2**10000)
    # end = time.perf_counter()
    # print(end - start)


