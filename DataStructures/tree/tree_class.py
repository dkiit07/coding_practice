# Tree


# Node Class
class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Tree class with root as Instance Attribute
class Tree:

    def __init__(self, root=None):
        self.root = root

    def generate_tree_from_list(self, node_list):

        """
        :param node_list: list of nodes in level order
        :return: root node
        """

        i = 1
        temp_list = []
        new_node = Node(node_list[0])
        self.root = new_node
        temp_list.append(self.root)

        while i < len(node_list):
            temp_root = temp_list.pop(0)
            if node_list[i] is not 'NaN':
                temp_root.left = Node(node_list[i])
                temp_list.append(temp_root.left)
            if node_list[i+1] is not 'NaN':
                temp_root.right = Node(node_list[i+1])
                temp_list.append(temp_root.right)
            i += 2
        return self.root










