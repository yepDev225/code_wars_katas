def duplicate_count(text):
    occurs_dict = {}
    nb_of_l_rep = 0
    for char in text.lower():
        occurs_dict[char] = occurs_dict.get(char, 0) + 1
    for _ , value in occurs_dict.items():
        if value >= 2:
            nb_of_l_rep += 1
    print(occurs_dict)
    return nb_of_l_rep