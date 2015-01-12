#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        # binary search rows
        s = 0
        e = len(matrix) - 1
        while s <= e:
            mid = (s + e) / 2
            if matrix[mid][-1] < target:
                s = mid + 1
            elif matrix[mid][0] > target:
                e = mid - 1
            else:
                break
        if s <= e:
            row = mid
        else:
            return False

        # binary search inside row
        s = 0
        e = len(matrix[row]) - 1
        while s <= e:
            mid = (s + e) / 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
s = Solution()
print s.searchMatrix(matrix, 3) # True
print s.searchMatrix(matrix, 16) # True
print s.searchMatrix(matrix, 15) # False