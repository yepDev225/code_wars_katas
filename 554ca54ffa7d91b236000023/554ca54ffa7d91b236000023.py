def delete_nth(order,max_e):
    dict = {}
    new_order = []
    for nb in order:
        if nb in dict.keys():
            if dict[nb] < max_e:
                dict[nb] +=1
                new_order.append(nb)
        else:
            dict[nb] = 1
            new_order.append(nb)
    return new_order