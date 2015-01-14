#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <assert.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return this->build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }

    TreeNode *build(vector<int> &preorder, int pl, int pr, vector<int> &inorder, int il, int ir) {
        if (pl > pr)
            return NULL;

        TreeNode *node = new TreeNode(preorder[pl]);
        int index = il;
        while (1) {
            if (inorder[index] == preorder[pl])
                break;
            index++;
        }
        int &root_index = index;
        node->left = build(preorder, pl + 1, pl + root_index - il, inorder, il, root_index - 1);
        node->right = build(preorder, pl + root_index - il + 1, pr, inorder, root_index + 1, ir);
        return node;
    }
};

void bfs(TreeNode *root) {
    if (root == NULL) {
        cout << "tree is empty!" << endl;
        return;
    }
    queue<TreeNode *> q;
    q.push(root);
    int cur = 1;
    int next = 0;
    int count = 0;
    while (!q.empty()) {
        TreeNode *node = static_cast<TreeNode *>(q.front());
        q.pop();
        cout << node->val;
        count++;
        if (node->left) {
            q.push(node->left);
            next++;
        }
        if (node->right) {
            q.push(node->right);
            next++;
        }
        if (count == cur) {
            cout << endl;
            count = 0;
            cur = next;
        }
    }
}

int main(int argc, char **argv) {
    Solution s;
    int pre_seq[] = {1,2,4,3,5,6};
    int in_seq[] = {2,4,1,5,3,6};
    vector<int> preorder(pre_seq, pre_seq + 6);
    vector<int> inorder(in_seq, in_seq + 6);
    TreeNode *node = s.buildTree(preorder, inorder);
    cout << "pinrt binary tree in bfs" << endl;
    bfs(node);

    return 0;
}
