#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int> &num) {
        if (num.size() == 0)
            return -1; // or exception

        int start = 0;
        int end = num.size() - 1;
        while(start < end) {
            int mid = (start + end) / 2;
            if (num[mid] < num[end])
                end = mid;
            else
                start = mid + 1;
        }
        return num[start];
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {4, 5, 6, 7, -1453, 1, 2};
    vector<int> case1(arr, arr + 7);
    assert(-1453 == s.findMin(case1));
    int arr2[] = {6, 7, -1453, 1, 2, 4, 5};
    vector<int> case2(arr2, arr2 + 7);
    assert(-1453 == s.findMin(case2));
    int arr3[] = {2,1};
    vector<int> case3(arr3, arr3 + 2);
    assert(1 == s.findMin(case3));

    return 0;
}
