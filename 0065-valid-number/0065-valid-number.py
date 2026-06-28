class Solution(object):
    def isNumber(self, s):
        state = 0
        for c in s:
            if c.isdigit():
                if state == 0 or state == 1 or state == 2:
                    state = 2
                elif state == 3 or state == 4 or state == 5:
                    state = 4
                elif state == 6 or state == 7 or state == 8:
                    state = 8
                else:
                    return False
            elif c == '+' or c == '-':

                if state == 0:
                    state = 1
                elif state == 6:
                    state = 7
                else:
                    return False
            elif c == '.':
                if state == 0 or state == 1:
                    state = 3
                elif state == 2:
                    state = 5
                else:
                    return False

            elif c == '+' or c == '-':
                if state == 0:
                    state = 1
                elif state == 6:
                    state = 7
                else:
                    return False
            elif c == '.':
                if state == 0 or state == 1:
                    state = 3
                elif state == 2:
                    state = 5
                else:
                    return False
            elif c == 'e' or c == 'E':
                if state == 2 or state == 4 or state == 5:
                    state = 6
                else:
                    return False
            else:
                return False
        
        return state in [2, 4, 5, 8]
            
                
        


       
        