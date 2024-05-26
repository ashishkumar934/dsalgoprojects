from binary_tree_implementation import TreeNode, TreeOperations
from collections import deque


class DepthFirstTraversal(TreeOperations):
    @staticmethod
    def print_tree_depth_first_traversal_stack_method(root_node):
        tracking_stack=deque('')

        # inorder traversal (root, left, right)

    @staticmethod
    def print_tree_depth_first_traversal_recursion_method(root_node: TreeNode):
        # inorder traversal (root, left, right)
        if root_node is None:
            return
        else:
            root_node.print_value()
            DepthFirstTraversal.print_tree_depth_first_traversal_recursion_method(root_node.left)
            DepthFirstTraversal.print_tree_depth_first_traversal_recursion_method(root_node.right)


if __name__ == '__main__':
    sample_tree = TreeNode(2)
    sample_tree.left = (TreeNode(3))
    sample_tree.right = (TreeNode(5))
    sample_tree.left.left = (TreeNode(6))
    sample_tree.left.right = (TreeNode(7))
    sample_tree.left.right.left = (TreeNode(8))
    sample_tree.left.right.left = (TreeNode(9))
    sample_tree.left.right.right = (TreeNode(10))
    TreeOperations.print_tree_depth_first_traversal(sample_tree)
    print("-------DepthFirstTraversal--------Recursion--------")
    DepthFirstTraversal.print_tree_depth_first_traversal_recursion_method(sample_tree)
