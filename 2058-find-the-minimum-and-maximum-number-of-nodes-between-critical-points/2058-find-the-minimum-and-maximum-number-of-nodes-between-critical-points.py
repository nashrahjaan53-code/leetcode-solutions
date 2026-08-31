# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        critical = []
        prev = head
        curr = head.next
        pos = 1
        while curr.next:
            if(curr.val > prev.val and curr.val > curr.next.val) or \
              (curr.val < prev.val and curr.val <curr.next.val):
              critical.append(pos)
            prev = curr
            curr = curr.next
            pos += 1
        if len(critical) < 2:
            return [-1, -1]
        min_dist = min(critical[i] - critical[i-1] for i in range(1,len(critical)))
        max_dist = critical[-1] - critical[0]
        return [min_dist, max_dist]
       





        