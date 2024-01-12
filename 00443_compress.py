"""
https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Complexity Time: O(n), Space O(1)
    def compress(self, chars: list[str]) -> int:
        i, comp = 0, 0
        while i < len(chars):
            group_len = 1
            while (i + group_len) < len(chars) and chars[i + group_len] == chars[i]:
                group_len += 1
            chars[comp] = chars[i]
            comp += 1
            if group_len > 1:
                str_group_len = str(group_len)
                chars[comp:comp+len(str_group_len)] = list(str_group_len)
                comp += len(str_group_len)
            i += group_len

        return comp
             






