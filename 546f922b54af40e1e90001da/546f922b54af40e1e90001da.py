def alphabet_position(text):
    temp = []
    for i in range(len(text)):
        if text[i].isalpha():
            nb = str(ord(text[i].lower()) - ord("a") + 1)
            temp.append(nb + " ") 
    return "".join(temp).strip()