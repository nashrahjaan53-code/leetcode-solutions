class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        perfix = strs[0]

        for i in range(1,len(strs)):
            while not strs[i].startswith(perfix):
                perfix = perfix[:-1]
                if not perfix:
                    return ""
        return perfix
        



        