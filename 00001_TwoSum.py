"""
https://leetcode.com/problems/two-sum/description/

"""

# # 1. Brute Force 
# # Time complexity O(n^2)
# # Space complexity O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] + nums[i] == target:
#                     return [i, j]