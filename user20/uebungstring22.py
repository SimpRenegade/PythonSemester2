print("Übung3")
str = "Ich habe mir eingeschissen"
l1 = str.split()
for x in l1:
    print(x)
print(l1)
print()
print("Übung4")
dict_schulden = {"Len": "5€", "Ole": "10€", "Rone": "7000€"}

file = open("DictFile.txt", "w")
for key, value in dict_schulden.items():
    file.write('%s:%s\n' % (key, value))
file.close()
print(dict_schulden.items())
