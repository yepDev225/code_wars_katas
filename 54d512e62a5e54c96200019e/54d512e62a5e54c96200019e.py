def prime_factors(n):
    diviser = {}
    while n > 1:
        for p in range(2, int(n**0.5)+1):
            if n % p == 0:
                diviser[p] = diviser.get(p, 0) + 1
                n = int(n/p)
                break
        else:
            diviser[n] = diviser.get(n, 0) + 1
            break
    str = ""
    for key, value in diviser.items():
        str= str + f"({key}**{value})" if value > 1 else str + f"({key})" 
    return str