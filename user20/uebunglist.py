print("Übung1")
li = [3, 6, 4, 8, 55, 7, 33, 99, 23, 22, 666, 333]
print(li)
li[0] = 666
print(li)
li = [47, 6, 4, 8, 55, 7, 33, 99, 23, 22, 666, 333]
print("Übung2")
del li[2:7]
#li22 = list(range(0, 8, 1))
li23 = [3, 6, 2, 7, 3, 73, 3, 7]
print(li)
#li[3:5] = list(range(0, 8, 1))
#print(li22)
for x in li23:
    li.insert(3, x)
#li.insert(3:6) = 435, 3424, 6775, 324, 7567, 234, 6456, 24
print(li)
print("Übung3")
print("a)")
li.append(424)
li.append(345)
li.append(6756)
li.append(53)
li.append(6546)
print(li)
print("b)")
#li2 = [424, 345, 6756, 53, 6546]
#li.extend(li2)
print("Übung4")
del li[0]
print(li)
print("Übung5")
li.reverse()
print(li)
print("Übung6")
print("Übung7")
li2 = [424, 345, 6756, 53, 6546]
li7 = []
for x in li:
     li7.append(x * 10)
print(li7)