#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in xrange(len(A)):
            num = A[i]
            while num > 0 and num < len(A)+1 and num != A[num-1]:
                A[i] = A[num-1]
                A[num-1] = num
                num = A[i]
        for i in xrange(len(A)):
            if i+1 != A[i]:
                return i + 1
        return len(A) + 1

s = Solution()
print s.firstMissingPositive([3,4,-1,1]) # 2
print s.firstMissingPositive([1,2,0]) # 3
print s.firstMissingPositive([3,2,1,5,4]) # 6