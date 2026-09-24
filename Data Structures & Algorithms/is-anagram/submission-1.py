# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False
# return Counter(s) == Counter(t) Counter data structure here checks for occurences in a string 

        for ch in s:
            if ch not in dic1:
                dic1[ch] = 1
            else:
                dic1[ch] += 1
# countS[s[i]] = 1 + countS.get(s[i], 0) this returns key if exists otherwise defaults to 0 doesnt throw a key error.
        
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
                
# return sorted(s) == sorted(t) sorting can require space from O(n+m) to O(n) but increases time complexity
        