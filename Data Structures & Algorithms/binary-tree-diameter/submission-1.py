# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dbt(node):
            if not node:
                return 0, 0

            left_height, left_diam = dbt(node.left)
            right_height, right_diam = dbt(node.right)

            height = 1 + max(left_height , right_height)
            through_node = left_height + right_height
            diameter = max(through_node , left_diam, right_diam)  

            return height, diameter
        return dbt(root)[1]









