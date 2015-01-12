#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minPathSum(std::vector<std::vector<int> > &grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;

        int height = grid.size();
        int width = grid[0].size();

        for (int col = 1; col < width; col++) {
            grid[0][col] += grid[0][col-1];
        }
        for (int row = 1; row < height; row++) {
            grid[row][0] += grid[row-1][0];
        }
        for (int row = 1; row < height; row++)
            for (int col = 1; col < width; ++col)
            {
                grid[row][col] += std::min(grid[row-1][col], grid[row][col-1]);
            }

        return grid[height-1][width-1];
    }
};

int main(int argc, char **argv) {
    Solution s;

    int row1[] = {1,2,3};
    int row2[] = {3,2,4};
    int row3[] = {9,0,1};
    std::vector<int> v1(row1, row1 + sizeof(row1)/sizeof(row1[0]));
    std::vector<int> v2(row2, row2 + sizeof(row2)/sizeof(row2[0]));
    std::vector<int> v3(row3, row3 + sizeof(row3)/sizeof(row3[0]));
    std::vector<std::vector<int> > v;
    v.push_back(v1);
    v.push_back(v2);
    v.push_back(v3);

    int sum = s.minPathSum(v);
    std::cout << sum << std::endl;

    return 0;
}
