"""
https://www.lintcode.com/problem/1844/description
"""

from typing import (
    List,
)


class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        # write your code here
        prefix_sum = self.get_prefix_sum(nums)

        answer = float("inf")
        sum2index = {0: 0}
        for end in range(len(nums)):
            if prefix_sum[end + 1] - k in sum2index:
                subarray_len = end + 1 - sum2index[prefix_sum[end + 1] - k]
                answer = min(answer, subarray_len)
            sum2index[prefix_sum[end + 1]] = end + 1
        
        return -1 if answer == float("inf") else answer


    def get_prefix_sum(self, nums: List[int]):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
