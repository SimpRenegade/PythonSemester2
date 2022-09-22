import measure_mem

n = 10_000_000

print('generator')
g = (n for n in range(n))

measure_mem.show_memory()

