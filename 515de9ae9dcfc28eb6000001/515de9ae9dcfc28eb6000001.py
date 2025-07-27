def solution(s):
    len_s = len(s)
    split_s = []
    i = 0
    while i < len_s:
        i += 1 
        item = s[i-1]+s[i] if i < len_s else s[i-1]+"_"
        split_s.append(item)
        i += 1 
    return split_s