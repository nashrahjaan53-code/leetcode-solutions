class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)
        
        while i < n:

            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            

            num_words = j - i
            total_spaces = maxWidth - line_len
            

            if j == n or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:

                spaces_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)
                
                line = ''
                for k in range(i, j - 1):
                    line += words[k]
                    spaces = spaces_between + (1 if k - i < extra_spaces else 0)
                    line += ' ' * spaces
                line += words[j - 1]
            
            result.append(line)
            i = j
        
        return result




  
        
        