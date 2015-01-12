#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return []
        p0 = 0
        p2 = len(A) - 1
        pm = 0
        while pm <= p2 and p0 <= p2:
            if A[pm] == 0:
                A[pm] = A[p0]
                A[p0] = 0
                p0 += 1
                pm += 1
            elif A[pm] == 2:
                A[pm] = A[p2]
                A[p2] = 2
                p2 -= 1
            else:
                pm += 1
        return A

s = Solution()
print s.sortColors([0,2,2,1,0,2,1,2]) # [0,0,1,1,2,2,2,2]
print s.sortColors([1,0]) # [0,1]
print s.sortColors([1]) # [1]
print s.sortColors([0]) # [0]
print s.sortColors([1, 1]) # [1, 1]
print s.sortColors([1,2,0]) # [0,1,2]