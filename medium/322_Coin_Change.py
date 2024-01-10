class Solution:
    def __init__(self):
        self.mem = None

    def coin_change(self, coins, amount):
        if amount < 0: return math.inf
        if amount == 0: return 0
        if self.mem[amount] is not None:
            return self.mem[amount]        
        minimum = math.inf
        for coin in coins:
            minimum = min(minimum, 1 + self.coin_change(coins, amount - coin))
        self.mem[amount] = minimum
        return minimum


    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mem = [None for _ in range(amount + 1)]
        min_coin_change = self.coin_change(coins, amount)
        if min_coin_change == math.inf: return -1
        return min_coin_change
