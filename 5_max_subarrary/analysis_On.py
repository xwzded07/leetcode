#!/usr/bin/env python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        N = len(A)
        sum = A[0]
        min_sum = min(0, sum)
        max_subsum = sum
        for idx in xrange(1, N):
            sum += A[idx]
            print idx, min_sum, sum
            if sum - min_sum > max_subsum:
                max_subsum = sum - min_sum
            if sum < min_sum:
                min_sum = sum
                
        return max_subsum
            
        
s = Solution()
print s.maxSubArray([-2,-3,0,-1])
print s.maxSubArray([-3,-2,0,-1])
print s.maxSubArray([1,2])
