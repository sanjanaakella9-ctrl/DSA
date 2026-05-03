class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        index = 0
        profit = 0 
        for i in range(len(prices)):
         if prices[i] < min:
            min = prices[i]
            index = i 
         else:
            if (prices[i] - min) > profit:
                profit = prices[i] - min
        return profit
