#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if not matrix:
            return matrix

        n = len(matrix)

        for k in xrange(0, n/2):
            x = k
            for y in xrange(k, n-1-k):
                cx = x
                cy = y
                print cx, cy
                last = matrix[cx][cy]
                for t in xrange(0, 4):
                    nx = cy
                    ny = n - 1 - cx
                    tmp = matrix[nx][ny]
                    matrix[nx][ny] = last
                    last = tmp
                    cx = nx
                    cy = ny
        return matrix

s = Solution()
m1 = [[1]]
print s.rotate(m1) # [[1]]
m2 = [[1,4,7],[2,5,8],[3,6,9]]
print s.rotate(m2)
m3 = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
print s.rotate(m3)