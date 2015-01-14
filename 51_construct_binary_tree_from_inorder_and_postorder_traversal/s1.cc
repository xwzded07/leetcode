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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        return this->build(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }

    TreeNode *build(vector<int> &inorder, int il, int ir, vector<int> &postorder, int pl, int pr) {
        if (il > ir)
            return NULL;

        TreeNode *node = new TreeNode(postorder[pr]);
        int index = il;
        while (1) {
            if (inorder[index] == postorder[pr])
                break;
            index++;
        }
        node->left = build(inorder, il, index - 1, postorder, pl, pl + index - il -1);
        node->right = build(inorder, index + 1, ir, postorder, pl + index -il, pr - 1);
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
    int post_seq[] = {4,2,5,6,3,1};
    int in_seq[] = {2,4,1,5,3,6};
    vector<int> postorder(post_seq, post_seq + 6);
    vector<int> inorder(in_seq, in_seq + 6);
    TreeNode *node = s.buildTree(inorder, postorder);
    cout << "pinrt binary tree in bfs" << endl;
    bfs(node);

    return 0;
}
