#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};

class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval insertInterval) {
        std::vector<Interval> newIntervals;
        if (intervals.size() == 0)
            return newIntervals;

        for (vector<Interval>::iterator it = intervals.begin();
            it != intervals.end();
            it++) {
            if (insertInterval.start == -1) { // already inserted to new vector
                newIntervals.push_back(*it);
            } else {
                if (it->end < insertInterval.start) {
                    newIntervals.push_back(*it);
                } else if (it->start > insertInterval.end) {
                    newIntervals.push_back(insertInterval);
                    newIntervals.push_back(*it);
                    insertInterval.start = -1;
                } else {
                    insertInterval.start = min(insertInterval.start, it->start);
                    insertInterval.end = max(insertInterval.end, it->end);
                }
            }
        }
        return newIntervals;
    }
};

int main(int argc, char **argv) {
    Solution s;

    return 0;
}
