# Given an integer array nums and an integer k, return the k most frequent elements within the array.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output = {}
        

        for i in nums:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1

        l = sorted(output.keys(),key= lambda x : output[x] ,reverse=True) 

        return l[:k]

        # Pattern: HashMap + custom sort by frequency 
        # Time: O(n log n) | Space: O(n)