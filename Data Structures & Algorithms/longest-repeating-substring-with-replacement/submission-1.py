# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        store = {}
        length = 0
        freq = 0

        for r in range(len(s)):
            store[s[r]] = store.get(s[r], 0) + 1
            freq = max(freq, store[s[r]])

            while (r - l + 1) - freq > k:
                store[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)

        return length

# Pattern: Dynamic Sliding Window with frequency map (shrink when window_len - max_freq > k)
# Time: O(n) | Space: O(1)