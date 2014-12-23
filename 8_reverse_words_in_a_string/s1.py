#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if len(s) < 2:
            return s

        sl = list(s)
        s = 0
        e = 0
        while s < len(sl):
            while s < len(sl) and sl[s] == ' ':
                s += 1
            if s == len(sl):
                break
            e = s + 1
            while e < len(sl) and sl[e] != ' ':
                e += 1
            self.reversePart(sl, s, e-1)
            s = e + 1

        return ''.join(sl)
    def reversePart(self, l, s, e):
        if s >= len(l):
            return
        while s < e:
            tmp = l[s]
            l[s] = l[e]
            l[e] = tmp
            s += 1
            e -= 1
                    

s = Solution()
print s.reverseWords(" aha  ! let's  start coding!! ")
print s.reverseWords("ab")
print s.reverseWords("e ")
print s.reverseWords(" b")
