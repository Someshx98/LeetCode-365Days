def maxDepthAfterSplit(seq: str) -> list[int]:
    result = []
    if len(seq) == 0:
        return result

    count = []
    depth = 0
    d_p = []
    for ch in seq:
        if ch == '(':
            depth += 1
            d_p.append(depth)

        if ch == ')':
            d_p.append(depth)
            depth -= 1

    for x in d_p:
        temp = x % 2
        result.append(temp)

    return result

s = "(((()))((())))"

print(maxDepthAfterSplit(s))

# depth = 0
# x = []
#
# for ch in s:
#     if ch == "(":
#         depth += 1
#         x.append(depth)
#     else:
#         x.append(depth)
#         depth -= 1
#
# print(x)
