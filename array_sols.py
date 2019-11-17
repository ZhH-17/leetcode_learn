# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:52:44 2019

@author: zhang
"""

class Solution:
    def twoSum(self, nums, target):
        found_values = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if nums[i] in found_values:
                return [i, found_values[nums[i]]]
            found_values[a] = i
        return None
solution = Solution()
nums = [1,3,4,6,8,12,-2, 9, 8, 13, 21, 17]
target = 12
res = solution.twoSum(nums, target)
