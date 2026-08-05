class Solution:
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            method = stack.pop()
            for next_method in graph[method]:
                if not suspicious[next_method]:
                    suspicious[next_method] = True
                    stack.append(next_method)
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))
        result= []
        for i in range(n):
            if not suspicious[i]:
                result.append(i)
        return result






        