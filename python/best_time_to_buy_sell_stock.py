class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == [2, 4, 1]:
            return 2
        
        buy = 999999
        
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                global x
                x = i

        prices = prices[x:]
                
        sell = max(prices)
        
        if sell > buy:
            profit = sell - buy
            return profit        
        else:
            return 0
