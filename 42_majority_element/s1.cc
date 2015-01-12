#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int> &num) {
        if (num.size() == 0)
            return -1; // or exception

        int element = 0;
        int count = 0;
        for (int i = 0; i < num.size(); i++) {
            if (count == 0) {
                element = num[i];
                count += 1;
            } else {
                if (element == num[i])
                    count++;
                else
                    count--;
            }
        }
        assert(count);
        return element;
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {1,2,3,1,2,4,1};
    vector<int> num(arr, arr+7);
    int majority = s.majorityElement(num);
    cout << majority << endl;
    return 0;
}
