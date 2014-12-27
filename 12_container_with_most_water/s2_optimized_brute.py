#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        max_area = 0
        for i in xrange(0, len(height)):
            s = 0
            e = len(height) - 1
            area = 0
            while s != i or e != i:
                if i - s > e - i:
                    if height[s] > height[i]:
                        area = (i - s) * height[i]
                        break
                    else:
                        s += 1
                else:
                    if height[e] > height[i]:
                        area = (e - i) * height[i]
                        break
                    else:
                        e -= 1
            if area > max_area:
                max_area = area
        return max_area


s = Solution()
print s.maxArea([1,3,5,7,9]) # 10
print s.maxArea([452,314,9,357,466,26,463,365,364,71,457,198,369,233,229,362,252,135,444,299,316,291,238,264,361,367,238,191,238,180,291,190,494,152,399,460,179,215,178,43,138,135,241,7,221,322,222,473,457,166,124,125,458,214,389,319,81,128,362,172,160,5,214,154,158,466,467,189,181,497,232,319,132,325,179,205,499,401,178,308,67,154,433,377,368,175,49,450,155,411,474,315,269,188,469,427,154,288,468,335,285,200,155,270,377,334,475,228,235,154,36,154,308,469,32,29,144,81,479,299,344,305,114,113,493,436,392,148,224,360,335,362,412,490,132,141,176,107,369,263,113,405,418,274,375,302,303,371,235,134,171,431,439,137,45,284,73,289,432,150,2,120,12,414,462,144,56,139,103,277,254,217,183,172,343,410,326,498,281,61,132,452,345,423,442,390,207,15,31,492,165,33,112,177,448,74,173,356,65,277,133,172,346,168,344,41,78,23,39,360,436,23,164,281,446,106,23,5,122,55,497,139,88,461,169,388,388,342,244,453,471,230,125,169,398,322,210,477,197,249,189,133,272,353,267,70,312,290,76,286,345,73,425,286,35,446,174,423,141,271,228,464,1,206,134,251,380,344,80,77,446,269,62,70,475,329,141,139,120,69,425,317,142,202,103,29,149,278,304,142,49,385,106,402,443,240,5,323,437,86,252,235,207,314,305,182,144,298,173,116,367,98,433,362,301,37,391,302,167,48,296,68,433,402,322,228,495,327,51,284,413,303,19,121,469,176,155,113,475,329,81,342,279,15,204,80,404,448,234,423,496,382,491,281,285,313,9,132,140,412,268,406,67,139,379,36,315,34,2,290,215,83,485,495,450,41,427,354,489,14,277,337,396,120,470,33,285,331,165,278,95,285,184,162,424,63,199,240,449,201,382,165,284,219,160,235,261,87,441,102,453,71,292,350,43,262,383,329,446,401,107,41,186,143,204,111,58,403,203,7,456,437,24,240,157,184,327,418,124,121,372,77,44,164,279,87,427,163,268,225,64,375,266,102,370,470,65,428,225,268,288,181,206,312,274,363,349,453,133,473,426,5,402,470,22,182,58,301,197,178,26,113,406,292,215,276,115,281,57,192,49,345,374,107,157,0,322,6,305,307,331,232,313,86,54,335,268,464,136,317,143,14,430,49,306,145,325,273,426,234,466,328,79,192,287,89,44,110,95,349,417,279,433,82,365,488,269,485,452,257,302,95,271,232,144,430,229,322,203,8,56,21,188,488,213,475,77,109,437,24,459,355,303,392,289,168,232,59,153,185,316,307,132,440,391,129,370,121,451,425,129,359,447,317,347,12,144,276,122,82,301,433,289,104,177,78,125,410,137,130,447,306,438,79,246,329,208,468,302,11,393,431,223,192,100,422,205,97,199,327,179,352,260,468,456,437,46,81,199,36,212,146,342,2,78,440,331,138,408,486,2,153,417,225,346,370,499,403,467,198,230,498,402,342,318,359,131,364,292,183,252,356,329,446,358,259,386,42,398,146,28,400,300,297,477,498,19,476,401,338,27,483,336,429,177,154,288,308,371,433,491,123,289,173,422,148,432,308,42,182,307,70,82,459,219,59,457,239,388,210,77,415,193,266,344,370,420,485,30,143,270,374,119,59,47,41,59,331,201,101,14,8,23,448,467,243,360,276,334,248,486,411,163,179,177,359,401,450,196,432,93,466,306,64,26,205,105,437,36,159,391,402,167,414,203,135,9,63,263,195,311,250,107,326,429,136,185,331,86,382,115,32,348,421,448,226,126,406,164,14,65,55,269,232,321,324,219,183,387,483,378,50,85,485,376,14,474,61,197,412,295,164,296,496,85,245,222,63,151,238,430,68,145,51,152,467,375,224,150,262,207,28,164,292,366,40,158,340,453,208,104,249,372,401,97,310,146,319,225,149,410,7,69,55,58,221,22,285,445,24,399,4,405,63,148,271,103,159,463,57,367,67,158,91,468,255,401,466,426,479,467,336,486,36,392,45,258,266,330,55,143,230,60,48,145,208,319,249,367,282,306,86,201,316,178,170,71,431,488,497,410,456,186,249,492,430,146,102,48,328,158,191,410,70,239,56,130,410,305,498,44,463,436,246,279,114,268,350,398,256,199,160,212,385,409,57,315,55,11,364,236,21,407,146,91,147,202,74,409,7,72,454,322,8,200,101,475,320,303,225,76,3,385,141,240,147,50,56,54,61,272,290,435,179,289,378,178,491,452,88,351,376,42,173,237,94,275,212,414,430])