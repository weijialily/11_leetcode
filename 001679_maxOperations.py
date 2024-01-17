"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Time complexity O(nlogn), Space complexity O(1)
    # Sort input list first
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                r -= 1
                l += 1
            if nums[l] + nums[r] < k:
                l += 1
            if nums[l] + nums[r] > k:
                r -= 1
            
        return count
