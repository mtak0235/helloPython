# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        
        def start(A, B):
            if A.val < B:
                if A.right == None:
                    A.right = TreeNode(B)
                else:
                    start(A.right, B) 
            else:
                if A.left == None:
                    A.left = TreeNode(B)
                else:
                    start(A.left, B)
            return
        if root == None:   root = TreeNode(val)
        else:               start(root, val)
        return root
