# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# difficulty: medium

# Time: O(n)
# Space: O(n)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num in num_counts:
            idx = num_counts[num]
            buckets[idx].append(num)
        
        k_freq = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    if len(k_freq) == k:
                        return k_freq
                    else:
                        k_freq.append(num)
        
        return k_freq