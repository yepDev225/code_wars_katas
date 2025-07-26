def is_pangram(st):
    alph = "abcdefghijklmnopqrstuvwxyz"
    single_letter = ""
    for c in st.lower():
        if c.isalpha() and c not in single_letter:
            single_letter += c
    return "".join(sorted(single_letter)) == alph