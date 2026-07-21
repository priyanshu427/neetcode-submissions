# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)    
        return False

# In Python, a set IS a Hash Set. in a normal for python to look up a certain number it will go sequentially. 
# when a set get a element its run through a hash function. the element is converted memory address and is stored there.
# when we check for the same element python converts it into hash and looks straight for that memory address and checks if the element is there. this runs at a time complexity of O(1)

