        def sum_tree_and_sum(node):
            # An empty tree is a Sum Tree and its sum is 0
            if node is None:
                return True, 0
            
            # A leaf node is also considered a Sum Tree
            if node.left is None and node.right is None:
                return True, node.data
            
            # Recur for left and right subtrees
            is_left_sum_tree, left_sum = sum_tree_and_sum(node.left)
            is_right_sum_tree, right_sum = sum_tree_and_sum(node.right)
            
            # Node's data must be equal to the sum of the left and right subtree sums
            is_current_sum_tree = (is_left_sum_tree and is_right_sum_tree and node.data == left_sum + right_sum)
            
            # Total sum of the tree rooted at the current node
            total_sum = left_sum + right_sum + node.data
            
            return is_current_sum_tree, total_sum
        
        is_sum_tree, _ = sum_tree_and_sum(node)
        return is_sum_tree
