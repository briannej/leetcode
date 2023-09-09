#state machine & dp with 3 arrays
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        sold,reset,hold=[0]*(length+1),[0]*(length+1),[0]*(length+1)
        reset[0]=0
        hold[0]=sold[0]=float('-inf')
        for i in range(1,length+1):
            sold[i]=hold[i-1]+prices[i-1]
            reset[i]=max(sold[i-1],reset[i-1])
            hold[i]=max(hold[i-1],reset[i-1]-prices[i-1])
        print(sold,reset,hold)
        return max(sold[-1],reset[-1])



#state machine & 1D dp
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
