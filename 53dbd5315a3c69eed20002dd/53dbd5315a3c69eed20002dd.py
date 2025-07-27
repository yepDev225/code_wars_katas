def filter_list(l):
    intL = []
    for item in l:
        if type(item) == type(1):
            intL.append(item)
    return intL