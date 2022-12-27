# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(root, path):
            if not root:
                return 
            
            inorder(root.left, path)
            path.append(root.val)
            inorder(root.right, path)
            
        
        path = [] 
        inorder(root, path)

        def middleOut(path):
            if not path: 
                return 
            
            mid = len(path)//2 

            left = middleOut(path[:mid])
            right = middleOut(path[mid+1:])

            return TreeNode(path[mid], left, right)
        
        return middleOut(path)
