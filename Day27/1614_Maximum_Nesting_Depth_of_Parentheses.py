def maxDepth(s: str) ->  int:
    stack = []
    depth = 0
    result = 0
    maximum_closing = 0
    maximum_opening = 0

    for c in s:
        if c == "(" or c == ")":
            stack.append(c)
        else:
            continue
    print(stack)

    for res in stack:
        if res == "(":
            depth += 1
            result = max(result, depth)
        else:
            depth -= 1

    # for res in stack:
    #     if res == "(":
    #         maximum_opening += 1
    #     elif res == ")":
    #         break
    #
    # print(maximum_closing, maximum_opening)

    return result


string = "(5/(2/8))*(((4-1+9/1)*3)/(2+5))-4-1+5+2*(4/3-7)"

print(maxDepth(string))