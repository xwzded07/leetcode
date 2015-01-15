#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        sort(candidates.begin(), candidates.end());

        vector<int> candidates_count;
        candidates_count.reserve(candidates.size());
        candidates_count[candidates_count.size() - 1] = 1;
        for (int i = candidates_count.size() - 2; i >= 0; i--) {
            if (candidates[i] == candidates[i + 1])
            {
                candidates_count[i] = candidates_count[i + 1] + 1;
            } else {
                candidates_count[i] = 1;
            }
        }
        copy(candidates_count.begin(), candidates_count.end(), ostream_iterator<int>(cout, " "));
        vector< vector<int> > combinations;
        findCombinations(candidates, candidates_count, target, combinations);
        cout << endl;
        return combinations;
    }

    void findCombinations(vector<int> &candidates, vector<int> &candidates_count, int target, vector< vector<int> > &combinations) {
        // use static vars to reduce params
        static vector<int> combination;
        static int current = 0;

        if (current == candidates.size())
            return;

        int current_count = candidates_count[current];
        current += current_count;
        findCombinations(candidates, candidates_count, target, combinations);
        current -= current_count;
        int count = 0;
        while (count < candidates_count[current]) {
            if (candidates[current] == target) {
                combination.push_back(candidates[current]);
                combinations.push_back(candidates);
                copy(combination.begin(), combination.end(), ostream_iterator<int>(cout, " "));
                combination.pop_back();
                break;
            }
            if (candidates[current] < target) {
                target -= candidates[current];
                combination.push_back(candidates[current]);
                current += current_count;
                findCombinations(candidates, candidates_count, target, combinations);
                current -= current_count;
                count++;
            } else {
                break;
            }
        }
        for (; count > 0; count--) {
            target += candidates[current];
            combination.pop_back();
        }
    }


};

int main(int argc, char **argv) {
    Solution s;
    int arr[] = {10,1,2,7,6,1,5};
    vector<int> case1(arr, arr+sizeof(arr)/sizeof(arr[0]));
    vector<vector<int> > combinations = s.combinationSum(case1, 8);
    cout << combinations.size() << endl;

    std::set< std::vector<int> > expected_combinations;
    int comb1[] = {1,7};
    int comb2[] = {1,2,5};
    int comb3[] = {2,6};
    int comb4[] = {1,1,6};
    expected_combinations.insert(vector<int>(comb1, comb1 + sizeof(comb1)/sizeof(comb1[0])));
    expected_combinations.insert(vector<int>(comb2, comb2 + sizeof(comb2)/sizeof(comb2[0])));
    expected_combinations.insert(vector<int>(comb3, comb3 + sizeof(comb3)/sizeof(comb3[0])));
    expected_combinations.insert(vector<int>(comb4, comb4 + sizeof(comb4)/sizeof(comb4[0])));

    assert(combinations.size() == 4);
    for (int i = 0; i < combinations.size(); ++i)
    {
        assert(expected_combinations.find(combinations[i]) != expected_combinations.end());
    }

    return 0;
}
