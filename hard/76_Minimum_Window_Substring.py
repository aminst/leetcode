from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimum_start, minimum_end = 0, float('inf')
        missing = Counter(t)
        need_count = len(t)
        i, j = 0, 0
        while j < len(s):
            if s[j] not in missing:
                if s[i] not in missing:
                    i += 1 
                j += 1
                continue
            if missing[s[j]] > 0:
                need_count -= 1                
            missing[s[j]] -= 1
            if need_count == 0:
                while True:
                    if s[i] not in missing:
                        i += 1
                        continue
                    if missing[s[i]] >= 0:
                        break
                    if missing[s[i]] < 0:
                        missing[s[i]] += 1
                    i += 1
                if j - i < minimum_end - minimum_start:
                    minimum_start = i
                    minimum_end = j
            j += 1
        if minimum_end >= len(s):
            return ""
        return s[minimum_start:minimum_end+1]

"""
Question:
    * Substring that includes all the characters (count is important order is not)
    * minimum length

Solution:
    * Move second pointer until you find a solution
        * How to check this?
    * Move the first and second pointer and see if you find a smaller solution
    * Make the window smaller

"ADOBECODEBANC"
 ^    ^

need_count: how many we need in general. when it reaches zero it's good and update the max
missing_count[c]: how many of that character we still need. Might get negative


"""
