class Solution:
    def createStoneValToIndexMap(self, stones: List[int]):
        val2idx = dict()
        for i, stone in enumerate(stones):
            val2idx[stone] = i
        return val2idx

    def canCross(self, stones: List[int]) -> bool:
        stone_val2idx = self.createStoneValToIndexMap(stones)
        final_stone = stones[-1]
        mem = [set() for i in range(len(stones))]
        if stones[1] - stones[0] != 1:
            return False
        f = self.canReachStartingFromIndexWithIncomingSteps(1, 1, stones, stone_val2idx, mem)
        print(mem)
        return f
    
    def canReachStartingFromIndexWithIncomingSteps(self, index: int, steps: int, stones: List[int], val2idx, mem) -> bool:
        if index == len(stones) -1:
            return True
        if -1*steps in mem[index]:
            return False
        if steps in mem[index]:
            return True
        if steps > 1 and stones[index]+steps-1 in val2idx and self.canReachStartingFromIndexWithIncomingSteps(val2idx[stones[index]+steps-1], steps-1, stones, val2idx, mem):
            mem[index].add(steps)
            return True
        if stones[index]+steps in val2idx and self.canReachStartingFromIndexWithIncomingSteps(val2idx[stones[index]+steps], steps, stones, val2idx, mem):
            mem[index].add(steps)
            return True
        if stones[index]+steps+1 in val2idx and self.canReachStartingFromIndexWithIncomingSteps(val2idx[stones[index]+steps+1], steps+1, stones, val2idx, mem):
            mem[index].add(steps)
            return True
        mem[index].add(-1*steps)
        return False
