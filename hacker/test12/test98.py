# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST2(root, None, None)

    def isValidBST2(self, root: TreeNode, maxNode, minNode) -> bool:
        if root == None:
            return True
        if minNode != None and root.val >= minNode:
            return False

        if maxNode != None and root.val <= maxNode:
            return False

        return self.isValidBST2(root.left, maxNode, root.val) and self.isValidBST2(root.right, root.val, minNode)


