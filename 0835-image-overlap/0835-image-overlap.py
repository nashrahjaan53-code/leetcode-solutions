class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ones1 = [(i,j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 =[(i,j) for i in range(n) for j in range(n) if img2[i][j]]
        if not ones1 or not ones2:
            return 0
        count = {}
        for x1, y1 in ones1:
            for x2, y2 in ones2:
                dx = x1 - x2
                dy = y1 - y2
                key = (dx, dy)
                count[key] = count.get(key, 0) + 1
        return max(count.values())





        