#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        # M(i,j): is s[0:i] and p[0:j] match, i~[0, len(s)], j~[0, len(p)]
        M = [[None for j in xrange(0, len(p)+1)] for i in xrange(0, len(s)+1)]
        M[0][0] = True
        for i in xrange(1, len(s)+1):
            M[i][0] = False
        for j in xrange(1, len(p)+1):
            M[0][j] = M[0][j-1] and p[j-1] == '*'
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] == '*':
                    M[i][j] = M[i-1][j-1] or M[i][j-1] or M[i-1][j]
                elif p[j-1] == '?':
                    M[i][j] = M[i-1][j-1]
                else:
                    M[i][j] = M[i-1][j-1] and p[j-1] == s[i-1]
        return M[len(s)][len(p)]


s = Solution()
print s.isMatch("aa","a") # false
print s.isMatch("aa","aa") # true
print s.isMatch("aaa","aa") # false
print s.isMatch("aa", "*") # true
print s.isMatch("aa", "a*") # true
print s.isMatch("ab", "?*") # true
print s.isMatch("aab", "c*a*b") # false                   
