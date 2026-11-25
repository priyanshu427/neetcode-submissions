# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmin, kmax = 1, max(piles)
        res = kmax

        while kmin <= kmax:
            mid = kmin + (kmax - kmin) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                res = mid
                kmax = mid - 1
            else:
                kmin = mid + 1

        return res
# Pattern: Binary Search on Answer Range [1 .. max(piles)] with ceiling division
# Time: O(n log m) | Space: O(1)