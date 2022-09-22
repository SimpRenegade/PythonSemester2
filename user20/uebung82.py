t = (1, 4.2342342, 4, 4, 5.32424, "sfsfds", 3, 43, 34, "dfsdfsf", 53, 7.4234, 2)
print(t[1])
print()
t2 = t[1:len(t)-1]
print(t2)
print()
t3 = (t + t + t)
print(t3)
print()
t3 = t3[::-1]
print(t3)
print()
t4 = t3[::2]
print()
print("Ist in t3 enthalten?")
print("sfsfds" in t3)