# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        def sumTree(root: Optional[TreeNode]):
            if not root: 
                return 0 
            
            root.val = sumTree(root.left) + sumTree(root.right) + root.val
            return root.val

        
        def checkSeverance(root, treeSum):
            if not root: 
                return False 

            if (
                (root.left and treeSum - root.left.val == root.left.val) or 
                (root.right and treeSum - root.right.val == root.right.val) or
                checkSeverance(root.left, treeSum) or 
                checkSeverance(root.right, treeSum)
            ): 
                return True 
        
            return False
        
        treeSum = sumTree(root)
        return checkSeverance(root, treeSum)

