class Solution:
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(coins)
        
        def count(x):
            res = 0
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]
                        if lcm > x:
                            valid = False
                            break
                if not valid:
                    continue
                if bits % 2 == 1:
                    res += x // lcm
                else:
                    res -= x // lcm
            return res
        
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
   





        