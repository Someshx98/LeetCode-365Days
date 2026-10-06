n = int(input("Enter the number of Parentheses: "))
orders = []

def answer(current, open, close):
    if len(current) == 2 * n:
        orders.append(current)
        return

    if open < n:
        answer(current + "(", open + 1, close)

    if close < open:
        answer(current + ")", open, close + 1)

answer("", 0, 0)

print(orders)