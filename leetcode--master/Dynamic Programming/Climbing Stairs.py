# -*- coding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.
你爬楼梯，到顶端有n阶阶梯
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
每次上升1或2步，你能有几种方法爬到顶
Note: Given n will be a positive integer.
给定n是一个正整数

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


# =============================================================================
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# =============================================================================
 
a = Solution()
b=a.climbStairs(6)
print(b)


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 1
        i,stairs1,stairs2 = 2,1,1
        while i <= n:
            stairs1 = stairs1 + stairs2
            if i == n:# n = 2 ，4时
                 print(stairs1)
                 return stairs1
            i += 1
            stairs2 = stairs1 + stairs2
            if i == n:# n = 3 ，5时
                 print(stairs2)
                 return stairs2
            i += 1

s = Solution()
c=s.climbStairs(6)

class Solution(object):
     def climbStairs(self, n):
         """
         :type n: int
         :rtype: int
         """
         if n == 1 or n == 0:
             return 1
         i,tmp1,tmp2 = 2,1,1
         while i <= n:
             tmp1 = tmp1 + tmp2
             if i == n:
                 return tmp1
             i += 1
             tmp2 = tmp1 + tmp2
             if i == n:
                 return tmp2
             i += 1

s = Solution()
d=s.climbStairs(6)
print(d)
