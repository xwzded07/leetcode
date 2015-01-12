#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return [1]

        carry = 1
        for idx in xrange(len(digits) - 1, -1, -1):
            if digits[idx] + carry >= 10:
                carry = (digits[idx] + carry) / 10
                digits[idx] = (digits[idx] + carry) % 10
            else:
                digits[idx] += carry
                carry = 0
                break
        if carry != 0:
            digits.insert(0, carry)
        return digits

s = Solution()
print s.plusOne([1,2,3,5]) # [1,2,3,6] 
print s.plusOne([1,3,9,9]) # [1,4,0,0]
print s.plusOne([9,9,9]) # [1,0,0,0]
print s.plusOne([0]) # [1]