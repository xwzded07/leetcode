#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    int findPeakElement(const vector<int> &num) {
        // linear solutino
        int i;
        for (i = 1; i < num.size(); i++)
            if (num[i] < num[i - 1])
                return i - 1;
        return num.size() - 1;
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
