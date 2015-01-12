#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]

        # find position pos of target
        s = 0
        e = len(A) - 1
        pos = -1
        while s <= e:
            mid = (s + e) / 2
            if A[mid] == target:
                break
            elif A[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        if s > e:
            return [-1, -1]
        else:
            pos = mid

        # find first ele in A[pos+1:] that is larger than target
        s = pos + 1
        e = len(A) - 1
        while s < e:
            mid = (s + e) / 2
            if A[mid] == target:
                s = mid + 1
            else:
                e = mid
        if A[e] == target:
            last = e
        else:
            last = e - 1

        # find last ele in A[0:pos] that is smaller than target
        s = 0
        e = pos - 1
        while s < e:
            mid = (s + e + 1) / 2
            if A[mid] == target:
                e = mid - 1
            else:
                s = mid
        if A[s] == target:
            first = s
        else:
            first = s + 1

        return [first, last]

s = Solution()
print s.searchRange([1], 1)
print s.searchRange([5, 7, 7, 8, 8, 10], 8) # [3, 4]
print s.searchRange([5, 7, 7, 8, 8, 8], 8) # [3, 5]
print s.searchRange([7, 7, 7, 8, 8, 8], 7) # [0, 2]
print s.searchRange([5, 7, 7, 8, 8, 10], 6) # [-1, -1]