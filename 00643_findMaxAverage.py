"""
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Complexity Time O(n), Space O(1)
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[0:k])
        for i in range(1, len(nums)-k+1):
            cur_sum = cur_sum - nums[i-1] + nums[i+k-1]
            max_sum = max(cur_sum, max_sum)
        return max_sum/k

    # # Faster solution
    # def maxVowels(self, s: str, k: int) -> int:
    #     vowels = frozenset("aeiou")
    #     cnt = ans = sum(s[i] in vowels for i in range(k))
    #     if ans != k:
    #         for i in range(k, len(s)):
    #             cnt += (s[i] in vowels) - (s[i - k] in vowels)
    #             ans = max(cnt, ans)
    #     return ans
