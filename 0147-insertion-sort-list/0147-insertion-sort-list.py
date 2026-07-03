class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        

        dummy = ListNode(0)
        dummy.next = head
        
        current = head.next
        head.next = None  
        
        while current:
            next_node = current.next
            

            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            

            current.next = prev.next
            prev.next = current
            
            current = next_node
        
        return dummy.next



        



        

 
        


            



     
            



            

        
        return dummy.next







        


        