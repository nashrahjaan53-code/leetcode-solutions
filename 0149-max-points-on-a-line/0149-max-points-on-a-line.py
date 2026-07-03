from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            
            for j in range(n):
                if i == j:
                    continue
                
                x2, y2 = points[j]
                dy = y2 - y1
                dx = x2 - x1
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                slopes[(dy, dx)] += 1
            
            if slopes:
                max_points = max(max_points, max(slopes.values()) + 1)
        
        return max_points





        