# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root, v, d):
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        depth = 0
        q = [root]

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if depth == d - 1:
                    cached_left = node.left
                    cached_right = node.right
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    node.left.left = cached_left
                    node.right.right = cached_right
            if depth == d - 1:
                break

        return root
