class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max, buying_candidate, selling_candidate = 0, prices[0], prices[0]
        
        for i, n in enumerate(prices):
            if n > selling_candidate:
                selling_candidate = n
            
            if n < buying_candidate or i == len(prices)-1:
                working_profit = selling_candidate - buying_candidate
                if profit_max < working_profit:
                    profit_max = working_profit
                buying_candidate = n
                selling_candidate = 0



        return profit_max
        