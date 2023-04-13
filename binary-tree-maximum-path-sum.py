# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans  = float("-inf")
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            ans = max(ans , (left+right+ root.val))
            
            better = max(left ,right) + root.val
            
            return better

        dfs(root)

        return ans