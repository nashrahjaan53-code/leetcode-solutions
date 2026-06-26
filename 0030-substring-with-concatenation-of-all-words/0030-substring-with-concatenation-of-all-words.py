from collections import Counter

class Solution:
    def findSubstring(self, s , words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        
        result = []
        
        
        for offset in range(word_len):
            seen = {}
            left = offset
            count = 0
            
            
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                 
                    if count == num_words:
                        result.append(left)
                        
                       
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    
                    seen.clear()
                    count = 0
                    left = right + word_len
        
        return result




        
 
      
     
 




      
       

            
           
               
               
                



                    
                    
            

    


        
      
        
        
        
        