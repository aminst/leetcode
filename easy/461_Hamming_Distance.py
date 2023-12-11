class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor != 0:
            if xor % 2 == 1:
                count += 1
            xor = xor >> 1
        return count
