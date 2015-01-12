#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S:
            return []

        subsets = []
        S.sort()
        for num in xrange(0, (1 << len(S))):
            bins = bin(num)
            subset = []
            for digit in xrange(0, len(bins) - 2):
                if bins[-digit-1] == '1':
                    subset.append(S[digit])
            subsets.append(subset)
                

        return subsets

s = Solution()
print s.subsets([1,2,3])
"""
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""