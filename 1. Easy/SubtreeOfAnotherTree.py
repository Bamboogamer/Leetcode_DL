# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Question: https://leetcode.com/problems/subtree-of-another-tree/
# ANSWER: https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)

class Solution:
    def isMatch(self, givenTree, subTree):
        if not (givenTree and subTree):
            return givenTree is subTree

        return givenTree.val == subTree.val and \
               self.isMatch(givenTree.left, subTree.left) and \
               self.isMatch(givenTree.right, subTree.right)

    def isSubtree(self, givenTree, subTree):

        # If the
        if not givenTree:
            return False
        if self.isMatch(givenTree, subTree):
            return True

        return self.isSubtree(givenTree.left, subTree) or self.isSubtree(givenTree.right, subTree)
