"""
https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # # 1. Brute Force
        # # Time complexity O(n^2)
        # # Space complexity O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] + nums[i] == target:
        #             return [i, j]

        # 2. One-pass Hash Table
        # Time complexity O(n)
        # Space complexity O(n)
        hashmap = {}
        for idx in range(len(nums)):
            res = target - nums[idx]
            if res in hashmap:
                return [idx, hashmap[res]]
            hashmap[nums[idx]] = idx


nums = [2, 7, 11, 15]
target = 9
output = Solution()
print(output.twoSum(nums, target))
