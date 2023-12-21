"""
https://leetcode.com/problems/two-sum-iii-data-structure-design/
"""


class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)
        return None

    def find(self, value: int) -> bool:
        idx_start, idx_end = 0, len(self.nums)-1
        while idx_start < idx_end:
            twosum = self.nums[idx_start] + self.nums[idx_end]
            if twosum == value:
                return True
            elif twosum < value:
                idx_start += 1
            else:
                idx_end -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(1)
obj.add(2)
obj.add(5)
param_2 = obj.find(6)
print(param_2)
