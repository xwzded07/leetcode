#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if not S:
            return []

        S.sort()
        counts = {}
        count = 1
        for i in xrange(len(S)-2, -1, -1):
            if S[i] == S[i+1]:
                count += 1
                del S[i+1]
            elif count != 1:
                counts[S[i]] = count
                count = 1
        if count != 1:
            counts[S[0]] = count

        subsets = []
        for num in xrange(0, (1 << len(S))):
            cur_sets = [[]]
            bin_str = bin(num)
            bin_str = bin_str[len(bin_str)-1:1:-1]
            for digit in xrange(0, len(bin_str)):
                if bin_str[digit] == '0':
                    continue
                if S[digit] not in counts:
                    for cur_set in cur_sets:
                        cur_set.append(S[digit])
                else:
                    length = len(cur_sets)
                    for i in xrange(0, length):
                        cur_sets[i].append(S[digit])
                        for j in xrange(1, counts[S[digit]]):
                            cur_sets.append(cur_sets[i] + [S[digit] for k in xrange(0, j)])

            subsets.extend(cur_sets)

        return subsets




s = Solution()
print s.subsetsWithDup([1,2,3,2]) # 
print s.subsetsWithDup([1,1])