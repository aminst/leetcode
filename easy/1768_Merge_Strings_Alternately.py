class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        min_overlap = min(word1_len, word2_len)
        final_str = ""
        for i in range(min_overlap):
            final_str += word1[i]
            final_str += word2[i]
        if word1_len > min_overlap:
            final_str += word1[min_overlap:]
        if word2_len > min_overlap:
            final_str += word2[min_overlap:]
        return final_str
