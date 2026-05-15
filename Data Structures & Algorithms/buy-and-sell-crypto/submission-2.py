class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # maxProfit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxProfit = max(profit, maxProfit)
        #     else:
        #         l = r
        #     r += 1

        maxProfit = 0
        minBuy = prices[0]

        for price in prices:
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(price, minBuy)

        return maxProfit