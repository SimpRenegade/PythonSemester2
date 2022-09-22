from packageübung.functions import col
from packageübung.functions import dic_coords
from packageübung.functions import sum_lists
from packageübung.functions import sum_dic
from packageübung.functions import table_dic
import math
print("Übung1")


# col


xs, ys = col()
print(xs[:5])
print()
print(ys[:5])

print("\n" + "Übung2")


# dic_coords


data = dic_coords(xs, ys)
print()
print(data)

# table_dic


table_dic(data)

print("\n" + "Übung3")

# sum_lists


sumlist1, sumlist2 = sum_lists(xs, ys)
print(sumlist1)
print(sumlist2)


# sum_dic


sumdic = sum_dic(data)
print(sumdic)
vergleich = (88.05864783223778, 120.76800430133447)
print(sum_lists(xs, ys) == sum_dic(data) == vergleich)
print("\n" + "Übung4")
print("funktioniert")


class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = math.sqrt(self.x*self.x + self.y*self.y)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y}"

    def __add__(coord1, coord2):
        return Coord(coord1.x + coord2.x, coord1.y + coord2.y)


coord1 = Coord(3, 4)
print(coord1.__repr__())
print("Die Distanze zum Nullpunkt beträgt {} Einheiten.".format(coord1.dist))


coord2 = Coord(6, 8)
print(coord2.__repr__())
print("Die Distanze zum Nullpunkt beträgt {} Einheiten.".format(coord2.dist))

sumCoord = coord1 + coord2
print(sumCoord.__repr__())