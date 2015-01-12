#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []

        row = [1]
        for i in xrange(1, rowIndex+1):
            for k in xrange(0, i-1):
                row[k] = row[k] + row[k + 1]
            row.insert(0, 1)

        return row

s = Solution()
print s.getRow(3) # [1,3,3,1] 