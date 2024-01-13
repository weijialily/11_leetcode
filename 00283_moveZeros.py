"""
https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Complexity Time O(n), Space O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reader, writer = 0, 0
        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1 
        nums[writer:] = [0]*(len(nums)-writer)

        # # Simpler but slightly slower, maybe because of swap values
        # n = len(nums)
        # i = 0
        # for j in range(n):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
