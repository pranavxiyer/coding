# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# difficulty: easy

# Time: O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_map:
                return [num_map[diff], i]
            num_map[n] = i
        
        return []