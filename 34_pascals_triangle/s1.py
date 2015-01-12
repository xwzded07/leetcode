#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <= 0:
            return []

        triangle = [[1]]
        for i in xrange(1, numRows):
            row = [1]
            for k in xrange(1, i):
                row.append(triangle[i-1][k-1] + triangle[i-1][k])
            row.append(1)
            triangle.append(row)
        return triangle

s = Solution()
print s.generate(5) 
"""[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]"""