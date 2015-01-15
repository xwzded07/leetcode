#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int> > combinations;
        sort(candidates.begin(), candidates.end());
        this->findCombination(candidates, target, combinations);

        return combinations;
    }

    void findCombination(vector<int> &candidates, int target, vector<vector<int> > &combinations) {
        static vector<int> combination;
        static int cur; // current candidate
        static int sum; // current sum

        if (cur == candidates.size()) // used all candidates
            return;

        if (sum + candidates[cur] == target) {
            combination.push_back(candidates[cur]);
            combinations.push_back(combination);
            combination.pop_back();
        } else if (sum + candidates[cur] < target) {
            sum += candidates[cur];
            combination.push_back(candidates[cur]);
            findCombination(candidates, target, combinations);
            combination.pop_back();
            sum -= candidates[cur];

            cur++;
            findCombination(candidates, target, combinations);
            cur--;            
        }    
    }
};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {2,3,6,7};
    vector<int> case1(arr, arr+sizeof(arr)/sizeof(arr[0]));
    vector<vector<int> > combinations = s.combinationSum(case1, 7);
    assert(combinations.size() == 2);
    assert(combinations[0].size() == 3);
    assert(combinations[0][0] == 2);
    assert(combinations[0][1] == 2);
    assert(combinations[0][2] == 3);
    assert(combinations[1].size() == 1);
    assert(combinations[1][0] == 7);
    return 0;
}
