class Solution:
    def reverseBits(self, n):
        binary = format(n,"b")
        res = 0
        
        missing_zeros = 32-len(binary) 
        
        for i in range(len(binary)):
            res += (int(binary[i]))*(2**(i+missing_zeros))
        return res
