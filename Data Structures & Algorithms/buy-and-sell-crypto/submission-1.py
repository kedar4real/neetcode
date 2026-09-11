class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy=prices[0]
        max_p=0
        for sell in prices:
            max_p=max(max_p,sell-min_buy)
            min_buy=min(min_buy,sell)
        return max_p
        
