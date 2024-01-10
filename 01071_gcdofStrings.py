"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
"""
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # # Brute force
        # # Time complexity: O(min(m,n)*(m+n))
        # # Space complexity: O(m+n)
        # len1, len2 = len(str1), len(str2)
        # base = ""
        # for i in range(min(len1, len2), 0, -1):
        #     if not (len1 % i or len2 % i):
        #         n1, n2 = len1 // i,  len2 // i
        #         if str1 == n1*str1[:i] and str2 == n2*str1[:i]:
        #             base = str1[:i]
        #             break
        # return base
   
        # GCD of numbers
        # Time complexity: O(m+n)
        # Space complexity: O(m+n)
        len1, len2 = len(str1), len(str2)
        base = ""
        if str1 + str2 == str2 + str1:
            k = math.gcd(len1, len2)
            base = str1[:k]
        return base
