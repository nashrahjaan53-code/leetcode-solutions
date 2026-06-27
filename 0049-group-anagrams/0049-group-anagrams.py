class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict

        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            anagram_map[key].append(s)

        return list(anagram_map.values())

        
       

      
        