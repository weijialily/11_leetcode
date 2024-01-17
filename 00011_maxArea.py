"""
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Complexity: Time O(n), Space O(1)
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r and l < len(height) and r < len(height):
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
