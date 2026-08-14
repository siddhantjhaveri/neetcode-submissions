class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            buy = prices[i-1]
            if prices[i-1]>prices[i]:
                buy = prices[i]
            else:
                profit += prices[i] - buy
        return profit

        