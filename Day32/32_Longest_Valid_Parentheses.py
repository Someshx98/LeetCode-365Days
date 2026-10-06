def longestValidParentheses(s: str) -> int:
    def validString(string):
        stack = []
        valid_idx = set()

        for idx, char in enumerate(string):
            if char == '(':
                stack.append(idx)

            elif char == ')' and stack:
                valid_idx.add(stack.pop())
                valid_idx.add(idx)

        return "".join(
            ch if i in valid_idx else "-" for i, ch in enumerate(string)
        )
    valid_parentheses = validString(s)
    print(valid_parentheses)
    count = 0
    maximum = 0
    for ch in valid_parentheses:
        if ch != "-":
            count += 1
            maximum = max(count, maximum)

        else:
            count = 0

    return maximum
x = "()(()"
print(longestValidParentheses(x))