class Solution:
    def reverseParentheses(self, s):
        stack = []
        for c in s:
            if c == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)
        return "".join(stack)