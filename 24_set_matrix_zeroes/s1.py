#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return

        h = len(matrix)
        w = len(matrix[0])

        flag_row = -1
        for row in xrange(0, h):
            for col in xrange(0, w):
                if matrix[row][col] == 0:
                    flag_row = row
                    break
            if flag_row != -1:
                break

        if flag_row == -1: # no element is 0
            return

        for row in xrange(0, h):
            if row == flag_row:
                continue
            row_set = False
            for col in xrange(0, w):
                if matrix[row][col] == 0:
                    matrix[flag_row][col] = 0
                    row_set = True
            if row_set:
                for col in xrange(0, w):
                    matrix[row][col] = 0

        for col in xrange(0, w):
            if matrix[flag_row][col] == 0:
                for row in xrange(0, h):
                    matrix[row][col] = 0

        for col in xrange(0, w):
            matrix[flag_row][col] = 0


s = Solution()
matrix = [
    [1,0,1],
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
s.setZeroes(matrix) # 
print matrix