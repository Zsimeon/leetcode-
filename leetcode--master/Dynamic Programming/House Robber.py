# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:47:33 2018

@author: Administrator
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.
你是一名专业的强盗，计划抢劫沿街的房屋。 每间房屋都藏有一定数量的金钱，
唯一阻止你抢劫每间房屋的限制因素是相邻房屋有安保系统相连，
如果在同一晚上有两间相邻房屋被闯入，它将自动与警方联系。

Given a list of non-negative integers representing the amount of money 
of each house, determine the maximum amount of money you can rob tonight
 without alerting the police.
 给定一个代表每个房子的金额的非负整数列表，
 确定您可以在不警告警方的情况下在今晚抢走的最大金额
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums[0],nums[-1])
        money = [0] * len(nums)
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(nums[i] + money[i-2], money[i-1])
        return money[len(nums)-1]
    
a = Solution()
b=a.rob([-2,1,-3,4,-1,2,1,-5,4])
print(b)




################################
class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = last = 0
        for i in nums:
            last, now = now, max(i+last, now)
        return now
c = Solution1()
d=c.rob([-2,1,-3,4,-1,2,1,-5,4])
print(d)