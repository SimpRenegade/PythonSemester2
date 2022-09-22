import measure_mem

n = 10_000_000

print('list comprehension')
L = [n for n in range(n)]

measure_mem.show_memory()

