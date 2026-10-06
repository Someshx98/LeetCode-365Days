def scoreOfParentheses(s: str) -> int:
    # if not s:
    #     return 0
    #
    # score = 1
    # depth = 0
    # depth_list = []
    #
    # for char in s:
    #     if char == '(':
    #         depth += 1
    #         depth_list.append(depth)
    #     if char == ")":
    #         depth_list.append(depth)
    #         depth -= 1
    #
    # def countScore(depthList, currentScore):
    #     if len(depthList) == 2:
    #         currentScore *= 2
    #         depthList.pop()
    #         depthList.pop()
    #         return depthList, currentScore
    #
    #     maximum_depth = max(depthList)
    #
    #     for i in range(len(depthList)):
    #         if depthList[i] == maximum_depth:
    #             if depthList[i - 1] == depthList[i + 2]:
    #                 currentScore *= 2
    #                 depthList.pop(depthList.index(maximum_depth))
    #                 depthList.pop(depthList.index(maximum_depth))
    #
    #             if depthList[i + 1] == depthList[i + 2] == depthList[i + 3]:
    #                 currentScore += 1
    #                 depthList.pop(depthList.index(maximum_depth))
    #                 depthList.pop(depthList.index(maximum_depth))
    #
    #     return depthList, currentScore
    #
    # while len(depth_list) != 0:
    #     depth_list, score = countScore(depth_list, score)
    #
    # return score

    # stack = [0]
    #
    # for ch in s:
    #     if ch == '(':
    #         stack.append(0)
    #
    #     else:
    #         inner = stack.pop()
    #         stack[-1] += max(inner * 2, 1)
    #
    # return stack[0]

    score = 0
    depth = 0

    for i, ch in enumerate(s):
        if ch == "(":
            depth += 1

        else:
            depth -= 1
            if s[i - 1] == "(":
                score += 1 << depth

    return score

x = "(())(())"



print(scoreOfParentheses(x))