"""
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # Use build-in functions
        # Time complexity: O(n)
        # Space complexity: O(n)
        return " ".join(reversed(s.split()))

    # # Solutions from others
    # # Time complexity: O(n)
    # # Space complexity: O(n)
    # def reverseWords(self, s: str) -> str:
    #     # Coververt string to char array and trim spaces
    #     l = self.trim_space(s)

    #     # reverse the whole string
    #     self.reverse(l, 0, len(l) - 1)

    #     # reverse each word
    #     self.reverse_single_word(l)

    #     return "".join(l)
    
    # def trim_space(self, s: str) -> str:
    #     left, right = 0, len(s) - 1
    #     # Remove lead spaces
    #     while left <= right and s[left] == " ":
    #         left += 1
    #     # Remove end spaces
    #     while left <= right and s[right] == " ":
    #         right -= 1
    #     # Reduce multiple spaces to single one
    #     output = []
    #     while left <= right:
    #         if s[left] != " ":
    #             output.append(s[left])
    #         elif output[-1] != " ":
    #             output.append(s[left])
    #         left += 1

    #     return output

    # def reverse(self, l: list, left: int, right: int) -> None:
    #     while left < right:
    #         l[left], l[right] = l[right], l[left]
    #         left, right = left + 1, right - 1

    # def reverse_single_word(self, l: list) -> None:
    #     n = len(l)
    #     start = end = 0

    #     while start < n:
    #         # Go to the end of the word
    #         while end <n and l[end] != " ":
    #             end += 1
    #         # Reverse the word
    #         self.reverse(l, start, end - 1)
    #         # Move to the next word
    #         start = end + 1
    #         end += 1
