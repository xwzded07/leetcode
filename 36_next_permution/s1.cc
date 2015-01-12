#include <iostream>
#include <algorithm>
#include <vector>

class Solution {
public:
    void nextPermutation(std::vector<int> &num) {
        if (num.size() <= 1)
            return;

        for (int h = num.size()-2; h >= 0; h--) {
            // find the minimal number larger than num[h] in the right part
            int l = num.size()-1;
            for (; l > h && num[l] <= num[h]; l--);
            if (l != h) {
                std::swap(num[l], num[h]);
                std::reverse(num.begin()+h+1, num.end());
                return;
            }
        }
        std::reverse(num.begin(), num.end()); 
    }
};

// template <typename T>
void printVector(const std::vector<int> &v) {
    for (std::vector<int>::const_iterator it = v.begin(); it < v.end(); ++it)
    {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}

int main(int argc, char **argv) {
    Solution s;
    std::vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);

    for (int i = 0; i < 26; i++) {
        printVector(v);
        s.nextPermutation(v);
    }

    return 0;
}