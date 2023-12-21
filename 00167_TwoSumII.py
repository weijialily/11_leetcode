"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 1. Two Pointers
        # Time complexity O(n)
        # Space complexity O(1)
        idx_start, idx_end = 0, len(numbers)-1
        while idx_start < idx_end:
            current_sum = numbers[idx_start] + numbers[idx_end]
            if current_sum == target:
                return [idx_start+1, idx_end+1]
            elif current_sum < target:
                idx_start += 1
            else:
                idx_end -= 1
                
        # # 2. Dictionary
        # # Time complexity O(n)
        # # Space complexity O(n)
        # hashmap = {}
        # for i, num in enumerate(numbers):
        #     if target-num in hashmap:
        #         return [hashmap[target-num]+1, i+1]
        #     hashmap[num] = i


nums = [2, 7, 11, 15]
target = 9
output = Solution()
print(output.twoSum(nums, target))
