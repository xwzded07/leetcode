#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Solution:
    # @return a string
    def countAndSay(self, n):
        if n <= 0:
            return ''

        seq1 = '1'
        seq2 = ''
        
        for i in xrange(0, n-1):
            s = 0
            while s < len(seq1):
                e = s + 1
                while e < len(seq1) and seq1[e] == seq1[s]:
                    e += 1
                l = e - s
                seq2 += str(l)
                seq2 += seq1[s]
                s = e
            seq1 = seq2
            seq2 = ''
            
        return seq1
                

s = Solution()
print s.countAndSay(-1)
print s.countAndSay(0)
print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
print s.countAndSay(6)