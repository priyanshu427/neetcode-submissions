# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in dic:
                dic[key] = []

            dic[key].append(word)

        return list(dic.values())

# Pattern: HashMap grouping words by sorted string key
# Time: O(m * n log n) | Space: O(m * n)