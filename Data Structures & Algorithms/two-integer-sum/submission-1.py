# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j. You may assume that every input has exactly one pair of indices i and j that satisfy the condition. Return the answer with the smaller index first.
# need to use hashmap(dict) instead of set as set doesnt store values on the basis of indices

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for index,val in enumerate(nums):
            
            diff= target - val
            
            if diff in dic:
                return [dic[diff],index]
            
            dic[val] = index
            