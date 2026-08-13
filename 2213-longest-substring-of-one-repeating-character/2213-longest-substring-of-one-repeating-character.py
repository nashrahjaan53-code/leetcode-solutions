class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        class Node:
            __slots__ = ("l","r", "lmx", "rmx", "mx")
            def __init__(self, l, r):
                self.l = l
                self.r = r
                self.lmx = self.rmx = self.mx = 1
        class SegmentTree:
            def __init__(self, s):
                self.s = list(s)
                n = len(s)
                self.tr =[None] * (n * 4)
                self.build(1, 1, n)
            def build(self, u, l, r):
                self.tr[u] = Node(l,r)
                if l == r:
                    return
                mid =(l + r) // 2
                self.build(u << 1, l, mid)
                self.build(u << 1 | 1, mid + 1, r)
                self.pushup(u)
            def modify(self, u, x, v):
                if self.tr[u].l == self.tr[u].r:
                    self.s[x - 1] = v
                    return
                mid = (self.tr[u].l + self.tr[u].r) // 2
                if x <= mid:
                    self.modify(u << 1, x, v)
                else:
                    self.modify(u << 1 | 1, x, v)
                self.pushup(u)
            def pushup(self, u):
                root = self.tr[u]
                left = self.tr[u << 1]
                right = self.tr[u << 1 | 1]
                root.lmx = left.lmx
                root.rmx = right.rmx
                root.mx = left.mx if left.mx > right.mx else right.mx
                a = left.r - left.l + 1
                b = right.r - right.l + 1
                if self.s[left.r - 1] == self.s[right.l - 1]:
                    if left.lmx == a:
                        root.lmx += right.lmx
                    if right.rmx == b:
                        root.rmx += left.rmx
                    if left.rmx + right.lmx > root.mx:
                        root.mx = left.rmx + right.lmx
        tree = SegmentTree(s)
        ans = []
        for i in range(len(queryIndices)):
            tree.modify(1, queryIndices[i] + 1, queryCharacters[i])
            ans.append(tree.tr[1].mx)
        return ans
                   












       
        