from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        

        # pattern -> list of words matching this pattern
        pattern_to_words = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_to_words[pattern].append(word)
        

        # parents[word] = set of parent words that lead to this word in shortest path
        parents = defaultdict(set)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            level_size = len(queue)

            visited_this_level = defaultdict(set)
            
            for _ in range(level_size):
                word = queue.popleft()
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for next_word in pattern_to_words[pattern]:
                        if next_word == endWord:
                            found = True
                        
                        if next_word not in distance:
                            if next_word not in visited_this_level:
                                visited_this_level[next_word] = set()
                                queue.append(next_word)
                            visited_this_level[next_word].add(word)
            

            for word, parent_set in visited_this_level.items():
                distance[word] = distance.get(word, float('inf'))
                for parent in parent_set:
                    parents[word].add(parent)
        

        def dfs(word):
            if word == beginWord:
                return [[beginWord]]
            
            paths = []
            for parent in parents[word]:
                for path in dfs(parent):
                    paths.append(path + [word])
            return paths
        
        return dfs(endWord)







        