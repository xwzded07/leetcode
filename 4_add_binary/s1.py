#/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Would rather use ‘{0:b}.format(int(a,2) + int(b,2))’ in real world
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        sum = 0
        d = 1
        for i in xrange(len(a)-1, -1, -1):
            sum += int(a[i]) * d
            d *= 2
        d = 1
        for j in xrange(len(b)-1, -1, -1):
            sum += int(b[j]) * d
            d *= 2
        
        if sum == 0:
            return '0'
            
        result = ''
        while sum > 0:
            result += str(sum % 2)
            sum /= 2
        
        return result[::-1]
    
s = Solution()
print s.addBinary('100010100100101', '10101111011')    
            