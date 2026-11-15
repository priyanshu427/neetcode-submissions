# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix      
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

# Pattern: Two-pass Prefix & Postfix running product without division
# Time: O(n) | Space: O(1) extra space (excluding output array)