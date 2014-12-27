#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        height = len(matrix)
        width = len(matrix[0])
        h = [0 for col in xrange(0, width+1)]
        max_area = 0

        for row in xrange(0, height):
            for col in xrange(0, width):
                if matrix[row][col] == '1':
                    h[col] += 1
                else:
                    h[col] = 0

            s = []
            for col in xrange(0, width+1):
                if len(s) == 0 or h[s[-1]] <= h[col]:
                    s.append(col)
                else:
                    while len(s) > 0 and h[s[-1]] > h[col]:
                        top = s.pop()
                        w = col if len(s) == 0 else col - s[-1] - 1
                        max_area = max(max_area, w * h[top])
                    s.append(col)

        return max_area




s = Solution()
matrix = [['1', '1', '0', '1'], ['1', '1', '1', '1'], ['0', '1', '1', '1'], ['1', '0', '0', '1']]
for row in matrix:
    print row
print s.maximalRectangle(matrix) # 6
