# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        small = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                small = min(small, nums[l])
                break

            mid = l + (r - l) // 2
            small = min(small, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return small

# Pattern: Binary Search on Rotated Sorted Array (compare nums[mid] with nums[l] to locate sorted half)
# Time: O(log n) | Space: O(1)