class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy Approach
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

        # Time Complexity is O(n)
        # Space Complexity is O(1) no extra space created


    