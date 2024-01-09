"""
https://leetcode.com/problems/two-sum-iii-data-structure-design/
"""


class TwoSum:

    def __init__(self):
        """
        Initialize data structure.
        """
        self.nums = []
        self.is_sorted = False

    def add(self, number: int):
        """
        Add the number to existing data structure, and mantain the ascending order
        """
        self.nums.append(number)
        self.nums.sort()

    def find(self, value: int) -> bool:
        idx_low, idx_high = 0, len(self.nums)-1
        while idx_low < idx_high:
            twosum = self.nums[idx_low] + self.nums[idx_high]
            if twosum > value:
                idx_high -= 1
            elif twosum < value:
                idx_low += 1
            else: # twosum == value
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(1)
obj.add(2)
obj.add(5)
param_2 = obj.find(4)
print(param_2)
