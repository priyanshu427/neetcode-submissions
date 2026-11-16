# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1

        while first < last:
            while first < last and not s[first].isalnum():
                first += 1
            while first < last and not s[last].isalnum():
                last -= 1

            if s[first].lower() != s[last].lower():
                return False

            first += 1
            last -= 1

        return True
# Pattern: Converging Two Pointers with in-place .isalnum() and .lower() checks
# Time: O(n) | Space: O(1)