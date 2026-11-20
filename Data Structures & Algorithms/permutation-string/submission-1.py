# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        store1 = {}
        store2 = {}

        for i in range(len(s1)):
            store1[s1[i]] = store1.get(s1[i], 0) + 1
            store2[s2[i]] = store2.get(s2[i], 0) + 1

        if store1 == store2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            store2[s2[r]] = store2.get(s2[r], 0) + 1

            store2[s2[l]] -= 1
            if store2[s2[l]] == 0:
                del store2[s2[l]]
            l += 1

            if store1 == store2:
                return True

        return False


# Pattern: Fixed-Size Sliding Window comparing character frequency maps (store1 == store2)
# Time: O(n) | Space: O(1)
