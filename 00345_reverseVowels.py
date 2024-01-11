"""
https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
        return "".join(s)
