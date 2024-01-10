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
        Add the number to existing data structure, 
        and mantain the ascending order.
        """
        self.nums.append(number)
        self.nums.sort()

    # # Two pointers
    # def find(self, value: int) -> bool:
    #     idx_low, idx_high = 0, len(self.nums)-1
    #     while idx_low < idx_high:
    #         twosum = self.nums[idx_low] + self.nums[idx_high]
    #         if twosum > value:
    #             idx_high -= 1
    #         elif twosum < value:
    #             idx_low += 1
    #         else:  # twosum == value
    #             return True
    #     return False
     
    # Hashmap
    def find(self, value: int) -> bool:
        hashmap = {}
        for idx in range(len(self.nums)):
            res = value - self.nums[idx]
            if res in hashmap:
                return True
            else:
                hashmap[self.nums[idx]] = idx
        return False

# Hashmap solution beats 95.64% Leetcode users  
# class TwoSum(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.num_counts = {}


#     def add(self, number):
#         """
#         Add the number to an internal data structure..
#         :type number: int
#         :rtype: None
#         """
#         if number in self.num_counts:
#             self.num_counts[number] += 1
#         else:
#             self.num_counts[number] = 1

#     def find(self, value):
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         :type value: int
#         :rtype: bool
#         """
#         for num in self.num_counts.keys():
#             comple = value - num
#             if num != comple:
#                 if comple in self.num_counts:
#                     return True
#             elif self.num_counts[num] > 1:
#                 return True
#         return False

# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(1)
obj.add(2)
obj.add(5)
param_2 = obj.find(4)
print(param_2)
