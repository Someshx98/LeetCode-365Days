def checkValidString(s: str) -> bool:
    if not s:
        return True

    def depthList(string):
        low = 0
        high = 0

        depth_list = []

        for ch in string:
            if ch == "(":
                low += 1
                high += 1

            elif ch == ")":
                low -= 1
                high -= 1

            else:
                low -= 1
                high += 1

            if high < 0:
                return None

            low = max(low, 0)
            depth_list.append((low, high))

        return depth_list

    d_l = depthList(s)

    if d_l is None:
        return False

    return d_l[-1][0] == 0

x = "(*))"

print(checkValidString(x))