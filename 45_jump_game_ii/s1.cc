#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    int jump(int A[], int n) {
        if (n == 0)
            return -1;
        if (n == 1)
            return 0;

        int steps = 0;
        int last = 0;
        int curr = 0;
        for (int i = 0; curr < n - 1; i++) {
            if (i > last) {
                if (curr == last) 
                    return -1;
                last = curr;
                steps++;
            }
            curr = max(curr, i + A[i]);
        }
        return steps + 1;
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {2,3,1,1,4};
    assert(2 == s.jump(arr, 5));
    int arr2[] = {3,2,1,0,5};
    assert(-1 == s.jump(arr2, 5));
    return 0;
}
