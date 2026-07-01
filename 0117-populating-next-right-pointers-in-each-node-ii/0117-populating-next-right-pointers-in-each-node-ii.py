class Solution:
    def connect(self, root):
        if not root:
            return root
        

        head = root
        
        while head:
   
            dummy = Node(0)
            tail = dummy
            

            current = head
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next
            
 
            head = dummy.next
        
        return root















        