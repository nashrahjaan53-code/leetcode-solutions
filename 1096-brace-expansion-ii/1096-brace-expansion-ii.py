class Solution:
    def braceExpansionII(self, expression):
        def parse(s, i):
            # returns (set_of_words, next_index)
            res = set()
            curr = {""}  # current concatenation product
            
            while i < len(s) and s[i] != '}':
                if s[i] == '{':
                    inner, i = parse(s, i + 1)
                    # concatenate curr with inner
                    new_curr = set()
                    for a in curr:
                        for b in inner:
                            new_curr.add(a + b)
                    curr = new_curr
                elif s[i] == ',':
                    # union: add curr to res and reset curr
                    res |= curr
                    curr = {""}
                    i += 1
                else:
                    # letter
                    new_curr = set()
                    for a in curr:
                        new_curr.add(a + s[i])
                    curr = new_curr
                    i += 1
            
            res |= curr
            return res, i + 1  # skip '}'
        
        words, _ = parse(expression, 0)
        return sorted(words)





        