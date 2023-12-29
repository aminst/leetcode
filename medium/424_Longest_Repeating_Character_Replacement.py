from collections import defaultdict
class Solution:
    def is_correct(self, max_count, start, end, k):
        length = (end - start + 1)
        return length - max_count <= k


    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        count_map = defaultdict(int)
        max_count = 0
        max_len = 0
        for end in range(len(s)):
            count_map[s[end]] += 1
            max_count = max(max_count, count_map[s[end]])
            while not self.is_correct(max_count, start, end, k):
                count_map[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
