# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# difficulty: easy

# Time: O(n)
# Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        
        return False

s = Solution()

print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 2, 3, 1]))
    
