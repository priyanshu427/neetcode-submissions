# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the total amount of water that can be trapped between the bars.
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        maxp = 0
        for i in range(n):
            maxp = max(maxp, height[i])
            prefix[i] = maxp

        maxs = 0
        for j in range(n - 1, -1, -1):
            maxs = max(maxs, height[j])
            suffix[j] = maxs

        area = 0
        for i in range(n):
            area += min(prefix[i], suffix[i]) - height[i]

        return area

# Pattern: Prefix & Suffix Running Max arrays (water = min(left_max, right_max) - height)
# Time: O(n) | Space: O(n)