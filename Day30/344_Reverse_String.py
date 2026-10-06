def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    x = []
    for ch in s:
        x.append(ch)

    s.clear()

    for i in range(len(x)):
        s.append(x.pop())

    print(s)



sr = ["h","e","l","l","o"]
reverseString(sr)