#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    int findPeakElement(const vector<int> &num) {
        // log solution
        int start = 0;
        int end = num.size() - 1;
        while (start < end) {
            int mid1 = (start + end) / 2;
            int mid2 = mid1 + 1;
            if (num[mid1] < num[mid2])
                start = mid2;
            else
                end = mid1;
        }
        return start;
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {1, 2, 3, 1};
    vector<int> v1(arr, arr+4);
    assert(2 == s.findPeakElement(v1));
    int arr2[] = {2,4,1,3,6};
    std::vector<int> v2(arr2, arr2+5);
    assert(1 == s.findPeakElement(v2) || 4 == s.findPeakElement(v2));
    return 0;
}
