class Solution:
    def is_valid(self, s):
        return (
            s in [
                "1", "2", "3", "4", "5",
                "6", "7", "8", "9", "10",
                "11", "12", "13", "14", "15",
                "16", "17", "18", "19", "20",
                "21", "22", "23", "24", "25", "26"
            ]
        ) 

    def count_ways_starting_from_index(self, s, index):
        if index == len(s): return 1
        if self.mem[index] != None: return self.mem[index]
        count = 0
        if self.is_valid(s[index:index+1]):
            count += self.count_ways_starting_from_index(s, index + 1)
        if index + 1 < len(s) and self.is_valid(s[index:index+2]):
            count += self.count_ways_starting_from_index(s, index + 2)
        self.mem[index] = count
        return self.mem[index]

    def numDecodings(self, s: str) -> int:
        self.mem = [None] * len(s)
        return self.count_ways_starting_from_index(s, 0)
