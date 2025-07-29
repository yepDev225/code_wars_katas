from collections import Counter

def scramble(s1, s2):
    count_s1 = Counter(s1)
    for char in s2:
        if count_s1[char] == 0:
            return False
        count_s1[char] -= 1
    return True