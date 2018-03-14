# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:46:19 2018

@author: Administrator
Say you have an array for which the ith element is the price of a given stock on day i.
假设你有一个数组，其中第i个元素是第i天给定股票的价格
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
如果您只允许完成至多一笔交易（即买入一只股票并出售一只股票），则设计一种算法以找到最大利润。
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

# =============================================================================
# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if(len(prices)<1):
#             return 0
#         buy_price = prices[0]
#         max_profit = 0
#         for i in range(1, len(prices)):
#             buy_price = min(buy_price,prices[i])
#             max_profit = max(max_profit, prices[i] - buy_price)
#         return max_profit
#     
# a = Solution()
# b=a.maxProfit([7, 1, 5, 3, 6, 4])
# print(b)
# 
# =============================================================================

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
 
        maxProfit = 0
        minPrice  = prices[0]
         
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
 
        return maxProfit
    
a = Solution()
b=a.maxProfit([7, 1, 5, 3, 6, 4])
print(b)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    