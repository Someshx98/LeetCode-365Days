def minAddToMakeValid(s: str) -> int:
    # if len(s) == 0:
    #     return 0
    #
    # if len(s) == 1:
    #     return 1
    #
    # stack = []
    # unsolved_stack = []
    #
    # for ch in s:
    #     if ch == "(":
    #         stack.append(ch)
    #
    #     if ch == ")":
    #         if len(stack) > 0:
    #             stack.pop()
    #         else:
    #             unsolved_stack.append(ch)
    #
    # print(unsolved_stack)
    #
    #
    #
    # return max(len(unsolved_stack), len(stack))

    stack = []
    unsolved_stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if stack:
                stack.pop()
            else:
                unsolved_stack.append(ch)

    return len(stack) + len(unsolved_stack)

x = "()))"
print(minAddToMakeValid(x))