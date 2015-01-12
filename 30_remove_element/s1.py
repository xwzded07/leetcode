#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0

        s = 0
        e = len(A) - 1
        while s <= e:
            if A[s] == elem:
                tmp = A[s]
                A[s] = A[e]
                A[e] = tmp
                e -= 1
            else:
                s += 1
        return s

s = Solution()
print s.() # 