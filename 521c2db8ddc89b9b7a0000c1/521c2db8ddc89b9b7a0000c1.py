def snail(array):
    result = []

    while array and array[0]:
        result += array.pop(0)
        for row in array:
            if row:
                result.append(row.pop())
        if array:
            result += array.pop()[::-1]

        for row in reversed(array):
            if row:
                result.append(row.pop(0))

    return result