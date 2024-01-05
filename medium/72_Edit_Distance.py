class Solution:
    def __init__(self):
        self.mem = None

    def min_dist(self, word1, word2, i, j):
        if i == len(word1): return len(word2) - j
        if j == len(word2): return len(word1) - i
        if self.mem[i][j] is not None:
            return self.mem[i][j]
        if word1[i] == word2[j]: return self.min_dist(word1, word2, i + 1, j + 1)
        minimum = 1 + min(
            self.min_dist(word1, word2, i + 1, j), # remove
            self.min_dist(word1, word2, i, j + 1), # insert
            self.min_dist(word1, word2, i + 1, j + 1) # replace
        )
        self.mem[i][j] = minimum
        return minimum

    def minDistance(self, word1: str, word2: str) -> int:
        self.mem = [[None for _ in range(len(word2))] for _ in range(len(word1))]
        return self.min_dist(word1, word2, 0, 0)
