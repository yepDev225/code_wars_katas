def ips_between(start, end):
    s = start.split(".")
    e = end.split(".")
    ips_bet = 0
    j = 3
    for i in range(len(s)):
        print(f"{int(e[i])-int(s[i])}")
        ips_bet += ((int(e[i]) -  int(s[i])) * 256**j)
        j -= 1
    return ips_bet