#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int> &num) {
        if (num.size() == 0)
            return -1;

        int start = 0;
        int end = num.size() - 1;
        while (start < end) {
            int mid = (start + end) / 2;
            if (num[mid] < num[end])
                end = mid;
            else if (num[mid] > num[end])
                start = mid + 1;
            else
                end--;
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

    int arr4[] = {1,1};
    vector<int> case4(arr4, arr4 + 2);
    assert(1 == s.findMin(case4));

    int arr5[] = {3,1,1};
    vector<int> case5(arr5, arr5 + 3);
    assert(1 == s.findMin(case5));

    int arr6[] = {31,1,1,1,13,16,17};
    vector<int> case6(arr6, arr6 + 7);
    assert(1 == s.findMin(case6));

    return 0;
}
