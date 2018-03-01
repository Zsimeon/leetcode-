# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:19:49 2018

@author: Administrator
"""

#Given two sorted integer arrays nums1 and nums2, 
#merge nums2 into nums1 as one sorted array.
#给定两个两个排序的整数数组nums1和nums2，将nums2合并为nums1作为一个排序数组。

#Note:
#You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
#你可以假设nums1有足够的空间（大小大于或等于m + n）来保存nums2中的其他元素。 nums1和nums2中初始化的元素数量分别为m和n。

class Solution:
    def merge(self, A, m, B, n):
        """
        :type num1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead
        """
        index_total = m + n - 1
        indexA = m-1
        indexB = n-1
        
        while indexA >= 0 and indexB >= 0:
            if A[indexA] > B[indexB]:
                A[index_total] = A[indexA]
                indexA -= 1
            else:
                A[index_total] = B[indexB]
                indexB -= 1
            index_total -= 1
            
        if indexA >= 0:
            while indexA >= 0:
                A[index_total] = A[indexA]
                indexA -= 1
                index_total -= 1
        else:
            while indexB >= 0:
                A[index_total] = B[indexB]
                indexB -= 1
                index_total -= 1
                