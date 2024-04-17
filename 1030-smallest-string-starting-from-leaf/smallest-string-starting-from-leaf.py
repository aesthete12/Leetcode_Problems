# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root):
        self.ans = None
        self.dfs(root, "")
        return self.ans

    def dfs(self, root, path):
        if not root:
            return

        path += chr(root.val + ord('a'))

        if not root.left and not root.right:
            if self.ans is None or path[::-1] < self.ans:  # Compare reversed paths
                self.ans = path[::-1]

        self.dfs(root.left, path)
        self.dfs(root.right, path)

       