def valid_braces(string):
    stack = []
    brackets = {"(":")", "[":"]", "{":"}"}

    for c in string:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if not stack or brackets[stack[-1]] != c:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False