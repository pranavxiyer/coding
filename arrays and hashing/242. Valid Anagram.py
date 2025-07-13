# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# difficulty: easy

# Time: O(n)
# Space: O(1)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            s_map = {}
            t_map = {}
            for i in range(len(s)):
                s_char = s[i]
                t_char = t[i]

                s_map[s_char] = s_map.get(s_char, 0) + 1
                t_map[t_char] = t_map.get(t_char, 0) + 1
        
        return s_map == t_map

s = Solution()
first = "anagram"
second = "nagaram"
print(s.isAnagram(first, second))