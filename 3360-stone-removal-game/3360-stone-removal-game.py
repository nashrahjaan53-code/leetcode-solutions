class Solution:
    def canAliceWin(self, n):
        if n < 10:
            return False
        stones = n
        curr = 10
        alice_turn = True
        while stones >= curr and curr > 0:
            stones -= curr
            curr -= 1
            alice_turn = not alice_turn
        return not alice_turn





        