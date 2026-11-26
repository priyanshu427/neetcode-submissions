# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        pivot = 0
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < nums[pivot]:
                    pivot = l
                break

            mid = l + (r - l) // 2
            if nums[pivot] > nums[mid]:
                pivot = mid
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        l = 0
        r = len(nums) - 1
        if target == nums[pivot]:
            return pivot
        elif target <= nums[r]:
            l = pivot + 1
        else:
            r = pivot - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

# Pattern: Binary Search on Rotated Sorted Array (locate sorted half and check target bounds)
# Time: O(log n) | Space: O(1)
