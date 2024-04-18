class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeOperations:

    @staticmethod
    def add_left_node(parent_node, given_node):
        parent_node.left = given_node

    @staticmethod
    def add_right_node(parent_node, given_node):
        parent_node.right = given_node

    @staticmethod
    # staticmethod don't have the self call. As it do not require the instance of the class to be invoked
    # This is the Pre Order Traversal using the Recursion Method
    def print_tree_depth_first_traversal(root):
        if root is None:
            return
        else:
            print(root.value)
            TreeOperations.print_tree(root.left)
            TreeOperations.print_tree(root.right)


if __name__ == '__main__':
    sample_tree = TreeNode(2)
    sample_tree.left = (TreeNode(3))
    sample_tree.right = (TreeNode(5))
    sample_tree.left.left = (TreeNode(6))
    TreeOperations.print_tree(sample_tree)
    # print(vars(sample_tree))

