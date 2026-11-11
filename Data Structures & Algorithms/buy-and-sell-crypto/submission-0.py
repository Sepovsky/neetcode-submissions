class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [prices[0]]
        for i in range(1, len(prices)):
            if buy[-1] > prices[i]:
                buy.append(prices[i])
            else:
                buy.append(buy[-1])
        
        sell = []
        for i in reversed(prices):
            if sell:
                if i > sell[-1]:
                    sell.append(i)
                else:
                    sell.append(sell[-1])
            
            else:
                sell.append(i)
        
        sell.reverse()
        ans = 0
        for i in range(len(buy)):
            ans = max(max(sell[i] - buy[i], ans), 0)
        return ans
