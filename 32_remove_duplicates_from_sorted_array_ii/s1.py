#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)

        p = 0
        for q in xrange(0, len(A)):
            if q + 2 < len(A) and A[q] == A[q+2]:
                pass
            else:
                A[p] = A[q]
                p += 1
        return p

s = Solution()
l = [1,1,2,3,4,4,4,5,6]
print s.removeDuplicates(l) # 8