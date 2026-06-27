class Solution:
    def rotateRight(self, head, k):
         if not head or not head.next or k == 0:
            return head
         length = 1
         last = head
         while last.next:
            last = last.next
            length += 1
         last.next = head
         k = k % length
         steps_to_new_last = length - k

         new_last = head
         for _ in range(steps_to_new_last - 1):
            new_last = new_last.next
         new_head = new_last.next
         new_last.next = None
        
         return new_head



     







      



  
       