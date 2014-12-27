#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        for level in xrange(1, len(triangle)):
            for pos in xrange(0, len(triangle[level])):
                last = None
                if pos - 1 >= 0 and pos - 1 < level:
                    last = triangle[level - 1][pos - 1]
                if pos < level:
                    if last:
                        last = min(last, triangle[level-1][pos])
                    else:
                        last = triangle[level-1][pos]
                triangle[level][pos] += last

        return min(triangle[-1])


triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s = Solution()
print s.minimumTotal(triangle) # 11 