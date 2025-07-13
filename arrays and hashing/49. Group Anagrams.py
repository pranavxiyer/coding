# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# difficulty: medium

# Time: O(m * n)
# Space: O(m * n)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}

        for word in strs:
            word_chars = [0 for i in range(26)]
            for char in word:
                word_chars[ord('a') - ord(char)] += 1
            
            grouping = tuple(word_chars)
            anagram_map[grouping] = anagram_map.get(grouping, []) + [word]
        
        anagrams = []
        for group in anagram_map:
            anagrams.append(anagram_map[group])
        return anagrams