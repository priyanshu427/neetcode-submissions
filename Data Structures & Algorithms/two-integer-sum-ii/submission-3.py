# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l=0
        r=len(numbers)-1

        while l < r:
            check = numbers[l] + numbers[r]
            if check > target:
                r -= 1
            elif check < target:
                    l += 1
            else:
                return [l + 1, r + 1]

# Pattern: Converging Two Pointers on a sorted array (adjust sum by moving L or R)
# Time: O(n) | Space: O(1)                


                

