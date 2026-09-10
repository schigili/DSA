class Solution:
    def averageOfSubtree(self, root: Optional['TreeNode']) -> int:
        self.count = 0
        
        def post_order(node):
            if not node:
                return 0, 0
            
            left_sum, left_num = post_order(node.left)
            right_sum, right_num = post_order(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_num = left_num + right_num + 1
            
            if total_sum // total_num == node.val:
                self.count += 1
                
            return total_sum, total_num
            
        post_order(root)
        return self.count