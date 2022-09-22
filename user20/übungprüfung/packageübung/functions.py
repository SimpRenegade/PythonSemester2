def col():
    with open("coords.txt", "r") as file:
        next(file)
        coordx = []
        coordy = []
        for x in file:
            x = x.strip()
            coordx.append(x.split(', ')[0])
            coordy.append(x.split(', ')[1])
        file.close()
        xs = coordx
        ys = coordy
        xs = [float(i) for i in xs]
        ys = [float(i) for i in ys]
    return xs, ys


def dic_coords(xs, ys):
    data = {"X": xs, "Y": ys}
    return data


def sum_lists(xs, ys):
    return sum(xs), sum(ys)


def sum_dic(data):
    output = ()
    keys = data.keys()
    for key in keys:
        output = output + (sum(data[key]),)
    return output


def sum_dict2(data):
    return tuple(sum(value) for value in data.values())


def table_dic(dic):
    with open("/home/user20/data/übungprüfung/table_dic.txt", "w") as File:
        i = 0
        File.write("{:<20} {:<20}\n".format('X-Koordinate', 'Y-Koordinate'))
        l1, l2 = dic.values()
        for x in l1:
            File.write("{:<20} : {:<20}\n".format(str(l1[i]), str(l2[i])))
            i = i + 1
