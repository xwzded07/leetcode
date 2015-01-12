#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
/**
 * Definition for an interval.
 */
struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
 };

bool interval_compare(const Interval &v1, const Interval &v2) {
    if (v1.start != v2.start)
        return v1.start < v2.start;
    else
        return v1.end < v2.end;
}

class Solution {
public:
    vector<Interval> merge(vector<Interval> &intervals) {
        if (intervals.size() <= 1)
            return intervals;

        std::vector<Interval> result;
        std::sort(intervals.begin(), intervals.end(), interval_compare);
        int s = 0, q = 0;
        int p = 1;
        while (p < intervals.size()) {
            if (intervals[q].end >= intervals[p].start) {
                if (intervals[q].end > intervals[p].end)
                    p++;
                else
                    q = p++;
            } else {
                result.push_back(Interval(intervals[s].start, intervals[q].end));
                s = q = p++;
            }
        }
        result.push_back(Interval(intervals[s].start, intervals[q].end));

        return result;
    }
};


int main(int argc, char **argv) {
    Solution s;
    std::vector<Interval> v;
    v.push_back(Interval(1,3));
    v.push_back(Interval(2,6));
    v.push_back(Interval(8,10));
    v.push_back(Interval(15,18));
    v.push_back(Interval(10,12));
    std::vector<Interval> result = s.merge(v);
    
    for (std::vector<Interval>::iterator it = result.begin(); it < result.end(); it++) {
        std::cout << it->start << " " << it->end << std::endl;
    }
    return 0;
}
