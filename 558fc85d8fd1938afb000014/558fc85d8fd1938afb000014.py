def sum_two_smallest_numbers(numbers):
    n1 = float("inf")
    n2 = float("inf")
    for nb in numbers:
        if nb < n1:
            n2 = n1
            n1 = nb
        elif nb < n2:
            n2 = nb
    return n1 + n2