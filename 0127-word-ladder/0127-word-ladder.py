from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        

        pattern_to_words = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_to_words[pattern].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            word, level = queue.popleft()
            
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                for next_word in pattern_to_words[pattern]:
                    if next_word == endWord:
                        return level + 1
                    
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        
        return 0







        