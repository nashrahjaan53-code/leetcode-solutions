class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:

            # Update histogram
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            extended = heights + [0]

            for i in range(len(extended)):
                while stack and extended[stack[-1]] > extended[i]:
                    h = extended[stack.pop()]

                    if stack:
                        w = i - stack[-1] - 1
                    else:
                        w = i

                    ans = max(ans, h * w)

                stack.append(i)

        return ans





        