# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.Return a list that contains the maximum element in the window at each step.
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque() 
        output = []

        for r in range(len(nums)):
            while window and nums[window[-1]] < nums[r]:
                window.pop()

            window.append(r)

            if window[0] < r - k + 1:
                window.popleft()

            if r >= k - 1:
                output.append(nums[window[0]])

        return output

# Pattern: Monotonic Decreasing Deque storing indices (O(1) amortized pop/push per element)
# Time: O(n) | Space: O(k)