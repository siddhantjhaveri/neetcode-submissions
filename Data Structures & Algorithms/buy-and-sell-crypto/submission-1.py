class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Brute Force
        # res = 0
        # for i in range(len(prices)-2):
        #     for j in range(i,len(prices)-1):
        #         res = max(res, prices[j]-prices[i])
        # return res
        ## Two pointer
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP