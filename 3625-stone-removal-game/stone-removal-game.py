class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        take = 10
        while n >= take and take > 0:
            n -= take
            take -= 1
            alice_turn = not alice_turn
        return not alice_turn