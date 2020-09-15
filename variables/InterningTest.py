import sys

if __name__ == "__main__":
    a = 'hello'
    b = 'hello'

    print(hex(id(a)), hex(id(b)))

    a = 'hello worldefefefewrf_AWFWE_FWE_FWFIIWFiwevjrir'
    b = 'hello worldefefefewrf_AWFWE_FWE_FWFIIWFiwevjrir'

    print(hex(id(a)), hex(id(b)), a is b)

    a = sys.intern('hello world')
    b = sys.intern('hello world')

    c = 'hello world'

    print(a, b, c)

    print(hex(id(a)))
    print(hex(id(b)))
    print(hex(id(c)))