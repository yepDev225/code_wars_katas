from collections import Counter
def comp(array1, array2):
    
    try:
        print(type(array1), type(array2))
        if array1 and array2:
            for x in array1:
                nb = Counter(array1)[x]
                nb_of_square = Counter(array2)[x*x]
                if nb_of_square != nb:
                    return False
            return True
        elif array1 == [] and array2 == []:
            return True
        else:
            return False
    except Exception as e:
        return False