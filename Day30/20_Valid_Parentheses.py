def isValid(s: str) -> bool:
    valid = []
    s_list = list(s)

    if not s_list:
        return True

    if s_list[0] in [")", "}", "]"]:
        return False

    if s_list[-1] in ["(", "{", "["]:
        return False

    while s_list:
        found = False

        for i in range(len(s_list) - 1):
            if s_list[i] == "(" and s_list[i + 1] == ")":
                valid.append("(")
                valid.append(")")

                s_list.pop(i)
                s_list.pop(i)

                found = True
                break

            elif s_list[i] == "[" and s_list[i + 1] == "]":
                valid.append("[")
                valid.append("]")

                s_list.pop(i)
                s_list.pop(i)

                found = True
                break

            elif s_list[i] == "{" and s_list[i + 1] == "}":
                valid.append("{")
                valid.append("}")

                s_list.pop(i)
                s_list.pop(i)

                found = True
                break

        if not found:
            return False

    return len(valid) == len(s)

sr = "(){}}{"

print(isValid(sr))