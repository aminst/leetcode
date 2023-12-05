# Solution 1 (BFS)
#class Solution:
#    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#        visited = [False for ch in s]
#        wordSet = set(wordDict)
#        queue = [0]
#        while len(queue) != 0:
#            start_index = queue.pop()
#            for i in range(start_index, len(s)):
#                if s[start_index:i+1] in wordSet:
#                    if i == len(s) - 1:
#                        return True
#                    if not visited[i+1]:
#                        visited[i+1] = True
#                        queue.append(i+1)
#        return False

# Solution 2 (DP Top down)
#class Solution:
#    def dp(self, end_index, s, wordSet, built):
#        if built[end_index-1] != None:
#            return built[end_index-1]
#        for word in wordSet:
#            if len(word) > end_index + 1:
#                continue
#            start_index = end_index - len(word) + 1
#            if s[start_index:end_index+1] != word:
#                continue
#            if start_index == 0:
#                return True
#            can_build = self.dp(start_index-1, s, wordSet, built)
#            if can_build:
#                built[start_index-1] = True
#                return True
#        built[end_index-1] = False
#        return False
#
#    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#        built = [None for i in range(len(s))]
#        return self.dp(len(s)-1, s, set(wordDict), built)

# Solution 3 (DP Buttom Up)
#class Solution:
#    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#        built = [False for i in range(len(s)+1)]
#        built[0] = True
#        for i in range(1, len(s)+1):
#            for word in wordDict:
#                if i < len(word):
#                    continue
#                if s[i-len(word):i] == word:
#                    if built[i-len(word)]:
#                        built[i] = True
#                        break
#        return built[len(s)]
