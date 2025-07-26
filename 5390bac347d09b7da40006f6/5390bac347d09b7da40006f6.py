def to_jaden_case(string):
    liste_of_words = string.split(" ")
    sts = ""
    for i in range(len(liste_of_words)):
        sts += liste_of_words[i].capitalize()+" " if i != len(liste_of_words) - 1 else liste_of_words[i].capitalize() 
    return sts