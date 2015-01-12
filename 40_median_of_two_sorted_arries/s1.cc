#include <vector>
#include <algorithm>
#include <iostream>
// using namespace std;

class Solution {
public:
    int find_kth(int *A, int m , int *B, int n, int k) {
        if (m == 0) {
            return B[k - 1];
        }
        if (n == 0) {
            return A[k - 1];
        }
        if (k == 1) {
            return std::min(A[0], B[0]);
        }

        int i = std::min(m, k / 2);
        int j = std::min(n, k / 2);
        if (A[i - 1] < B[j - 1])
            return find_kth(A + i, m - i, B, n, k - i);
        else
            return find_kth(A, m, B + j, n - j, k - j);
    }

    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        if ((m + n) % 2 == 0)
            return (find_kth(A, m, B, n, (m + n) / 2) + find_kth(A, m, B, n, (m + n) / 2 + 1)) / 2.0;
        else
            return find_kth(A, m, B, n, (m + n) / 2 + 1);
    }
};

int main(int argc, char **argv) {
    Solution s;
    int A[] = {1,3,5,7,9};
    int B[] = {2,4,6,8,10,19,35};
    double median = s.findMedianSortedArrays(A, sizeof(A)/sizeof(A[0]), B, sizeof(B)/sizeof(B[0]));

    int A2[] = {1};
    int B2[] = {1};
    median = s.findMedianSortedArrays(A2, sizeof(A2)/sizeof(A2[0]), B2, sizeof(B2)/sizeof(B2[0]));

    return 0;
}
