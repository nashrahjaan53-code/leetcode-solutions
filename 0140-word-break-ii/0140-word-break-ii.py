class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)
            
            memo[start] = sentences
            return sentences
        
        return backtrack(0)



       


        