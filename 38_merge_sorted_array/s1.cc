#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int r = m + n - 1;
        m--;
        n--;
        while (m >= 0 && n >= 0) {
            if (A[m] > B[n])
                A[r--] = A[m--];
            else
                A[r--] = B[n--];
        }
        while (n >= 0) {
            A[r--] = B[n--];
        }
    }
};

int main(int argc, char **argv) {
    Solution s;
    int A[] = {5,7,9,11,13,15,0,0,0,0,0,0};
    int B[] = {2,4,6,8,10,12};
    s.merge(A, 6, B, 6);

    // std::copy(path.begin(), path.end(), std::ostream_iterator<char>(std::cout, " "));
    for (int i = 0; i < sizeof(A)/sizeof(A[0]); ++i) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
