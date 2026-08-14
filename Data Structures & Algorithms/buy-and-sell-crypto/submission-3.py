class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        maxprofit = 0
        while s<len(prices):
            # print(prices[s] - prices[b])
            maxprofit = max(maxprofit, prices[s] - prices[b])
            if prices[b] > prices[s]:
                b=s
            s+=1
        return maxprofit