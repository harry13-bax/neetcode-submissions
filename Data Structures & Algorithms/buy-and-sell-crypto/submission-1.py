class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxi=0
        for i in range(len(prices)):
            if minprice>prices[i]:
                minprice=prices[i]
            else:
                profit=prices[i]-minprice
                if maxi<profit:
                    maxi=profit
        return maxi



        