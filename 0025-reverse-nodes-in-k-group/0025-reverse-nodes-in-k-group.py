class Solution:
    def reverseKGroup(self, head, k):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while count >= k:
             group_start = prev.next
             curr = group_start
             for _ in range(k - 1):
                next_node = curr.next
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
             prev = group_start
             count -= k
        
        return dummy.next

        
        

     
  



  





           


            




        
               
               
            

















        