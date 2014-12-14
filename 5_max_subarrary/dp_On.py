#!/usr/bin/env python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        N = len(A)
        presum = A[0]
        result = A[0]
        for idx in range(1, N):
            if presum > 0:
                presum += A[idx]    
            else:
                presum = A[idx]
            result = max(result, presum)
        return result
            
        
s = Solution()
print s.maxSubArray([-2,-3,0,-1])
print s.maxSubArray([-3,-2,0,-1])
print s.maxSubArray([1,2])
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
