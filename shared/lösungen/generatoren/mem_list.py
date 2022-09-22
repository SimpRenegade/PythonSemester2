import sys

import measure_mem

n = int(float(sys.argv[1]))

L = [x + 10 for x in range(n)]

measure_mem.show_memory()