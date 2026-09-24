# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False

        for ch in s:
            if ch not in dic1:
                dic1[ch] = 1
            else:
                dic1[ch] += 1

        for ch in t:
            if ch not in dic2:
                dic2[ch] = 1
            else:
                dic2[ch] += 1

        return dic1 == dic2 # directly evaluates to boolean
        # if dic1 == dic2:
        #     return True
        # else:
        #     return False
                
        