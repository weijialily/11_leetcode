"""
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)
        answer = [0]*nums_len
        answer[0] = 1
        for i in range(1, nums_len):
            answer[i] = nums[i-1] * answer[i-1]

        rightProduct = 1
        for i in range(nums_len-1, -1, -1):
            answer[i] = answer[i] * rightProduct
            rightProduct *= nums[i]
        
        return answer
