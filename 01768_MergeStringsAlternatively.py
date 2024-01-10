"""
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # # Two pointer solution
        # # Time complexity O(max(len_w1, len_w2))
        # # Space complexity O(len_w1+len_w2)
        # len_w1 = len(word1)
        # len_w2 = len(word2)
        # i, j = 0, 0
        # result = []
        # while i < len_w1 or j < len_w2:
        #     if i < len_w1:
        #         result += word1[i]
        #         i += 1
        #     if j < len_w2:
        #         result += word2[j]
        #         j += 1     
        # return "".join(result)

        # One pointer solution
        len_w1 = len(word1)
        len_w2 = len(word2)
        i = 0
        result = []
        for i in range(max(len_w1, len_w2)):
            if i < len_w1:
                result += word1[i]
            if i < len_w2:
                result += word2[i]
                i += 1

        return "".join(result)
