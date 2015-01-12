#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 1:
            return len(A)

        p = 1
        for q in xrange(1, len(A)):
            if A[q] != A[q-1]:
                A[p] = A[q]
                p += 1
        return p

s = Solution()
l = [1,1,2,3,4,4,4,5,6]
print s.removeDuplicates(l) # 6