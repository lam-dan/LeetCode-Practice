class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Keep track of recursive calls
        # index = i
        # running_total
        # count - for fewest number of coins
        # current_amount = coins[i]
        
        def dfs(i, running_total):
            #Base Case
            # running_total > amount
            # print("running_total", running_total)
            # print("Amount", amount)

            if running_total == amount:
                return 0
            if running_total > amount:
                return float(inf)
            if i >= len(coins):
                return float(inf)

            # Picking
            # print(i)
            # print(len(coins))
            
            pick = 1 + dfs(i, running_total + coins[i])
            # Not Picking
            not_pick = 0 + dfs(i + 1, running_total)

            return min(pick, not_pick)
        
        res = dfs(0,0)
        print("res", res)
            # return the min of the 2 above
        
        return res if res != inf else -1
