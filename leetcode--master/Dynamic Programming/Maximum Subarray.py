# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:24:57 2018

@author: Administrator
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
在数组中找到连续的子数组（至少包含一个数字），这个数组的总和最大。

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = g = -1000000000000
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g

    
a = Solution()
b=a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(b)


################################################

class Solution1:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = -2**31
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + nums[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum
    
c = Solution()
d=c.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(d)