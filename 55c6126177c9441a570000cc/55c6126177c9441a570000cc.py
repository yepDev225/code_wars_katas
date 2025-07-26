def order_weight(strng):
    weight_dict = {}
    array = strng.strip().split(" ")
    new_order_weight = ""
    for i in range(len(array)):
        nb = 0
        for d in array[i]:
            nb += int(d)
        array[i]= [array[i], nb]
    for item in sorted(sorted(array, key = lambda item: item[0]), key = lambda item: item[1]):
        new_order_weight += item[0]+" "
    return new_order_weight.strip()