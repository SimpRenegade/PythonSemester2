def read_coords(file_name):
    """Read space-seperated coolumns into two lists.

    Return two lists with float of x and y coordinates.
    """
    xs = []
    ys = []
    with open(file_name, 'r') as fobj:
        next(fobj)
        for line in fobj:
            temp = [float(value) for value in line.split(",")]
            xs.append(temp[0])
            ys.append(temp[1])
        fobj.close()
    return xs, ys


def dic_coords(xs, xy):
    """Attaches keys 'X' and 'Y' 
    and sorts values according to matched keys. 
    Reads data from a list.
    """
    data = {"X": xs, "Y": ys}
    return data


def read_as_dict(fname):
    """Attaches keys 'X' and 'Y'
    and sorts values according to matched keys.
    Reads data from a dictonary
    """
    data = {}
    with open(fname) as fobj:
        keys =[x.strip() for x in next(fobj).split(',')]
        for key in keys:
            data[key] = []
        for line in fobj:
            for key, value in zip(keys, line.split(',')):
                data[key].append(float(value))
    return data


def sum_list(xs, ys):
    """sums the values of the lists."""
    return(sum(xs), sum(ys))


def sum_dict(data):
    """sums the values of the lists in a dictionary."""
    keys = data.keys()
    output = ()
    for key in keys:
        output = output + (sum(data[key]),)
    return output