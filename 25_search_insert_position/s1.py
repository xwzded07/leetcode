#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return 0

        i = 0
        while i < len(A):
            if A[i] >= target:
                break
            i += 1

        return i

s = Solution()
print s.searchInsert([1,3,5,6],5) # 2 
print s.searchInsert([1,3,5,6],2) # 1
print s.searchInsert([1,3,5,6],7) # 4
print s.searchInsert([1,3,5,6],0) # 0