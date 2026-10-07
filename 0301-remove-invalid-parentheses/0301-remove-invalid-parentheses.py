class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(t):
            bal = 0
            for c in t:
                if c == '(':
                    bal += 1
                elif c == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0
        queue = [s]
        visited = {s}
        found = False
        res =[]
        while queue:
            next_level = []
            for curr in queue:
                if is_valid(curr):
                    res.append(curr)
                    found = True
                if found:
                    continue
                for i in  range(len(curr)):
                    if curr[i] not in '()':
                        continue
                    next_s = curr[:i] + curr[i+1:]
                    if next_s not in visited:
                        visited.add(next_s)
                        next_level.append(next_s)
            if found:
                break
            queue = next_level
        return res