#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        lookup = {}
        for idx in xrange(0, len(num)):
            if target - num[idx] in lookup:
                return (lookup[target-num[idx]]+1, idx+1)
            lookup[num[idx]] = idx



s = Solution()
print s.twoSum([1,5,3,8,4], 7) # (3, 5)
print s.twoSum([1,6], 7) # (1, 2)