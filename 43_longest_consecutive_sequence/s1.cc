#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_map<int,int> m;
        int longest = 0;
        for (int i = 0; i < num.size(); i++) {
            if (m.count(num[i]))
                continue;

            int upp = 0;
            int low = 0;
            if (m.count(num[i]-1))
                low = m[num[i]-1];
            if (m.count(num[i]+1))
                upp = m[num[i]+1];
            longest = max(longest, upp+low+1);

            m[num[i]] = 0;
            m[num[i]+upp] = upp+low+1;
            m[num[i]-low] = upp+low+1;
        }
        return longest;
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {100, 4, 200, 1, 3, 2};
    std::vector<int> v(arr, arr+6);
    int longest = s.longestConsecutive(v);
    cout << longest << endl;
    return 0;
}
