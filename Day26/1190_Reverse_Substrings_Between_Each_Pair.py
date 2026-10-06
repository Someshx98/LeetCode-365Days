def reverseParentheses(s: str) -> str:
    stack = []
    result = list(s)

    for i, ch in enumerate(result):
        if ch == '(':
            stack.append(i)

        elif ch == ")":
            start = stack.pop()

            result[start : i + 1] = result[start : i + 1][ : : -1]

    return "".join(c for c in result if c not in "()")

ex = "(ed(et(oc))el)"

print(reverseParentheses(ex))