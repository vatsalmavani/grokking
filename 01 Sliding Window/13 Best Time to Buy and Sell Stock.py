# LC: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# NC: https://youtu.be/1pkOgXD63yU

def maxProfit(prices):
    l = 0
    max_profit = 0
    for r in range(1, len(prices)):
        if prices[r] > prices[l]:
            window_profit = prices[r] - prices[l]
            max_profit = max(max_profit, window_profit)
        else:
            l = r
    return max_profit