import re

# My approach

# def evaluate(s: str, knowledge: list[list[str]]) -> str:
#     dct = dict(knowledge)
#     texts = re.findall(r"\((.*?)\)", s)
#
#     keys_list = dct.keys()
#
#     for text in texts:
#         if text in keys_list:
#             s = s.replace(f"({text})", dct[text])
#
#         else:
#             s = s.replace(f"({text})", "?")
#
#     return s


#  Better Approach

def evaluate(s: str, knowledge: list[list[str]]) -> str:
    dct = dict(knowledge)
    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == "(":
            j = s.index(")", i + 1)
            key = s[i + 1 : j]
            result.append(dct.get(key, "?"))
            i = j + 1

        else:
            result.append(s[i])
            i += 1

    return "".join(result)

s = "(a)(a)(a)aaa"
knowledge = [["a","yes"]]

print(evaluate(s, knowledge))

# dct = {
#     "a" : "b",
#     "c" : "d",
#     "e" : "f",
# }
#
# val = dct.keys()
#
# for i in val:
#     print(dct[i])