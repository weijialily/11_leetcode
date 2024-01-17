"""
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        res = False
        if len(s) > 0:
            while j < len(t) and i < len(s):
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i == len(s):
                res = True
        else:
            res = True

        return res
