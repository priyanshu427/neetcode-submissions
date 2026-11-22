# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
# You may assume that the correct output is always unique.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        store = {}
        for ch in t:
            store[ch] = store.get(ch, 0) + 1

        window = {}
        have, need = 0, len(store)
        res = [-1, -1]
        res_len = float("inf")  # equivalent of infinite
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in store and window[ch] == store[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in store and window[left_ch] < store[left_ch]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""


# Pattern: Dynamic Sliding Window with have/need distinct frequency counters
# Time: O(n + m) | Space: O(1)
