# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        seq = set(nums)
        length = len(seq)

        starts = []
        for num in seq:
            if (num - 1) not in seq:
                starts.append(num)

        best = 0
        for s in starts:
            count = 1
            curr = s
            for i in range(length):
                if (curr + 1) in seq:
                    count += 1
                    curr += 1
                else:
                    break

            if count > best:
                best = count

        return best
# Pattern: HashSet O(1) lookups starting only at sequence heads (num - 1 not in set)
# Time: O(n) | Space: O(n)
