#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1

        sum = m + n -2
        num = 1
        # [m...sum]
        for x in xrange(m, sum+1):
            num *= x
        # [1..n-1]
        for x in xrange(1, n):
            num /= x
            
        return num

s = Solution()
print s.uniquePaths(3, 7) # 28