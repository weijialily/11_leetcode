"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [x >= max_candies-extraCandies for x in candies]
