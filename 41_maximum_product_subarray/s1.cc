#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProduct(int A[], int n) {
        int max_prod = A[0];
        int min_prod = A[0];
        int result = max_prod;

        for (int i = 1; i < n; i++) {
            int max_tmp = max_prod;

            max_prod = max(A[i], A[i]*max_prod);
            max_prod = max(max_prod, A[i]*min_prod);

            min_prod = min(A[i], min_prod*A[i]);
            min_prod = min(min_prod, max_tmp*A[i]);

            result = max(result, max_prod);

        }
        return result;
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {2,3,-2,4};
    int prod = s.maxProduct(arr, 4);
    cout << prod << endl;
    int arr2[] = {2,-5,-2,-4,3};
    prod = s.maxProduct(arr2, 5);
    cout << prod << endl;
    return 0;
}
