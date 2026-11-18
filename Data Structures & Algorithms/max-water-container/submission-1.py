# You are given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        area = min(heights[l], heights[r]) * (r - l)

        while l < r:
            print(area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            narea = min(heights[l], heights[r]) * (r - l)
            if narea > area:
                area = narea
            else:
                continue
        return area


# Pattern: Greedy Converging Two Pointers (always advance the shorter height inward)
# Time: O(n) | Space: O(1)
