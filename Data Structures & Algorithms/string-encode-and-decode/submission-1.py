# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
class Solution:

    
    def encode(self, strs: List[str]) -> str:
        
        s = ""
        for i in strs:
            
            s +=  str(len(i)) + "#" + i 
        return s

    def decode(self, s: str) -> List[str]:

        output,i = [],0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i = j+1+length

        return output

# Pattern: Length-prefixed encoding (len + "#" + str) with two-pointer slicing
# Time: O(n) | Space: O(n)
        