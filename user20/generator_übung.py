# 13.3.1 Übung 1

print('13.3.1 Übung 1:')

g = (n*3 for n in range(21))
print(list(g))

# 13.3.2 Übung 2

print('13.3.2 Übung 2:')

g = (n for n in range(21) if n % 2 == 0)
print(list(g))

# 13.3.3 Übung 3

print('13.3.3 Übung 3:')


def numbers():
    print('10')
    for i in range(1, 10):
        yield 1
        print((str)(i * 100))


n = numbers()
while True:
    try:
        next(n)
    except StopIteration:
        break


# 13.3.4 Übung 4

print('13.3.4 Übung 4:')

import measure_mem

g = (n for n in range(10000))
g = (n for n in range(100000))
g = (n for n in range(1000000))

measure_mem.show_memory()

g = list(range(10000))
g = list(range(100000))
g = list(range(1000000))

measure_mem.show_memory()