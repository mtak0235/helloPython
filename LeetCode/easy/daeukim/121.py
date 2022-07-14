# 주식을 사고팔기 가장 좋은 시점

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_price = sys.maxsize
        
        for price in prices:
            low_price = min(low_price, price)
            max_profit = max(max_profit, price - low_price)
        return max_profit