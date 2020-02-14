# This program is to test the LinkedList class

from DataStructures.tree.tree_class import Tree


def main():


    tree = Tree()

    print('testing Tree Class')
    node_list = [1,2,3,4,'NaN',5,6]

    node_list = [1,2,6,'NaN',3,'NaN','NaN',4, 5]

    node_list = [314, 6, 6, 271, 561, 2, 271, 28, 0, 'NaN', 3, 'NaN', 1, 'NaN', 28, 'NaN','NaN','NaN','NaN',17, 'NaN', 401, 257, 'NaN','NaN','NaN','NaN','NaN',641]

    root = tree.generate_tree_from_list(node_list)

    print(root.right.left.right.left.right.val)



if __name__ == '__main__':
    main()

