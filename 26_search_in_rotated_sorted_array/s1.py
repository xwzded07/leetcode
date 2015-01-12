#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1

        first = 0
        last = len(A)-1
        while first <= last:
            mid = (first + last)/2
            if A[mid] == target:
                return mid
            if target < A[mid]:
                if A[mid] > A[first]: # type 1
                    if target >= A[first]:
                        last = mid - 1
                    else:
                        first = mid + 1
                elif A[mid] == A[first]: # unknown type
                    first += 1
                else: # type 2
                    last = mid - 1
            else:
                if A[mid] > A[first]: # type 1
                    first = mid + 1
                elif A[mid] == A[first]:
                    first += 1
                else: # type 2
                    if A[last] >= target:
                        first = mid + 1
                    else:
                        last = mid - 1

        return -1



s = Solution()
print s.search([4, 5, 6, 7, 0, 1, 2], 1) # 5
print s.search([4, 5, 6, 7, 0, 1, 2], 5) # 1
print s.search([4, 5, 6, 8, 0, 1, 2], 7) # -1
print s.search([1,1,1,1], 1) # 0