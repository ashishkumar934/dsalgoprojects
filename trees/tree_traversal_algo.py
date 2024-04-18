from binary_tree_implementation import TreeNode, TreeOperations
from collections import deque


class DepthFirstTraversal(TreeOperations):
    @staticmethod
    def print_tree_depth_first_traversal_stack_method(root_node):
        # inorder traversal (root, left, right)
        pass


if __name__ == '__main__':
    sample_tree = TreeNode(2)
    sample_tree.left = (TreeNode(3))
    sample_tree.right = (TreeNode(5))
    sample_tree.left.left = (TreeNode(6))
    TreeOperations.print_tree_depth_first_traversal(sample_tree)

    d = deque(['qewe','eewew'])
    print(d)
    print(len(d))
    print(d.maxlen)