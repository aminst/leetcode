class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        maximum = 0
        current_chars = set()
        while j < len(s):
            if s[j] not in current_chars:
                current_chars.add(s[j])
                maximum = max(maximum, j - i + 1)
            else:
                while s[j] in current_chars:
                    current_chars.remove(s[i])
                    i += 1
                current_chars.add(s[j])
            j += 1
        return maximum
