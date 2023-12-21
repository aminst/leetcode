class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def dfs(path_sum, prev, path=[]):
            if path_sum == target:
                print(path)
                combinations.append(path)
                return
            if path_sum > target:
                return
            for candidate in candidates:
                if candidate < prev: continue
                dfs(path_sum + candidate, candidate, path + [candidate])
        dfs(0, 0, [])
        return combinations
