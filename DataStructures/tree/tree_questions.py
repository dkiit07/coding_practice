from DataStructures.tree.tree_class import Tree


# prepare tree
tree = Tree()
# traversal
node_list = [314, 6, 6, 271, 561, 2, 271, 28, 0, 'NaN', 3, 'NaN', 1, 'NaN', 28, 'NaN','NaN','NaN','NaN',17, 'NaN', 401, 257, 'NaN','NaN','NaN','NaN','NaN',641]
node_list = ['A','B','I','C','F','J','O','D','E','NaN','G','NaN','K','NaN','P','NaN','NaN','NaN','NaN','H','NaN','L','N','NaN','NaN','NaN','NaN','NaN','M']
# height
node_list = ['A','B','K','C','H','L','O','D','G','I','J','M','N','NaN','NaN','E','F']
# height balanced
node_list = [1,2,3,4,'NaN','NaN','NaN','NaN',5]
# symmetric
# node_list = [1,2,2,'NaN',3,3]
# node_list = [1,2,2,3,4,4,3]
# node_list = [1,2,2,'NaN',3,'NaN',3]
# binary sum
# node_list = [1,0,1,0,1,0,0,0,1,'NaN',1,'NaN',0,'NaN',0,'NaN','NaN','NaN','NaN',0,'NaN',1,0,'NaN','NaN','NaN','NaN','NaN',1]
# sum
node_list = [1,2,3,4,6,'NaN','NaN','NaN',5]
# sum path
node_list = [1,2,3,4,6,'NaN',5,'NaN',5]

############################################################
root = tree.generate_tree_from_list(node_list)


# Traversal
############################################################
# 1. inorder
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(' {}'.format(root.val), end='')
    inorder_traversal(root.right)


############################################################
# 2. preorder
def preorder_traversal(root):
    if root is None:
        return
    print(' {}'.format(root.val), end='')
    preorder_traversal(root.left)
    preorder_traversal(root.right)


############################################################
# 3. postorder
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(' {}'.format(root.val), end='')


############################################################
# 4. Height of a Tree
def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))


############################################################
# 5. if the tree is height-balanced
def is_height_balanced(root):
    if root is None:
        return True
    if abs(height_of_tree(root.left) - height_of_tree(root.right)) > 1:
        return False
    else:
        return is_height_balanced(root.left) and is_height_balanced(root.right)


############################################################
# 6. if the tree is symmetric
def is_symmetric(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True

    def check_left_right(left, right):
        if left is None and right is None:
            return True

        if left is not None and right is not None and left.val != right.val:
            return False
        elif left is None or right is None:
            return False
        else:
            return check_left_right(left.left, right.right) and check_left_right(left.right, right.left)

    if root.left is not None and root.right is not None :
        return check_left_right(root.left, root.right)


############################################################
# 7. all path from root to leaf
def all_paths_from_root_to_leaf(root):
    path_list = []
    if root is None:
        return path_list
    temp_path = []

    def print_path(root, temp_path, path_list):
        if root is None:
            return
        temp_path.append(root.val)
        if root.left is None and root.right is None:
            path_list.append(temp_path.copy())

        print_path(root.left, temp_path, path_list)
        print_path(root.right, temp_path, path_list)
        temp_path.pop()

    print_path(root, temp_path, path_list)
    return path_list


############################################################
# 8. path from root to a given leaf node
def path_from_root_to_given_leaf(root, n):
    path = []
    return_path = []
    if root is None:
        return path

    def print_path(root, path, return_path):
        if root is None:
            return
        path.append(root.val)
        if root.val == n:
            return_path.append(path.copy())

        print_path(root.left, path, return_path)
        print_path(root.right, path, return_path)
        path.pop()

    print_path(root, path, return_path)
    return return_path[0]


############################################################
# 9. lowest common ancestor
def lowest_common_ancestor(root, n1, n2):
    if root is None:
        return None
    path1 = path_from_root_to_given_leaf(root, n1)
    path2 = path_from_root_to_given_leaf(root, n2)

    i = 0
    j = 0
    while i < len(path1) and j < len(path2):
        if path1[i] != path2[j]:
            break
        i += 1
        j += 1
    return path1[i-1]


############################################################
# 10. lowest common ancestor - recursive
def lca_recursivee(root, n1, n2):
    if root is None:
        return None

    if root.val == n1 or root.val == n2:
        return root

    left_lca = lca_recursivee(root.left, n1, n2)
    right_lca = lca_recursivee(root.right, n1, n2)

    if left_lca is not None and right_lca is not None:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca


############################################################
# 11. sum the root to leaf path binary
def sum_root_to_leaf_binary(root):
    path_sum = 0
    path_list = all_paths_from_root_to_leaf(root)

    for path in path_list:
        i = 0
        while i < len(path):
            path_sum += path[-1-i] * 2**i
            i += 1
    return path_sum


############################################################
# 12. sum the root to leaf path binary - recursive
def sum_root_to_leaf_binary_recursive(root):
    path_sum = 0
    if root is None:
        return 0

    def sum_paths(root, path_sum):
        if root is None:
            return 0
        path_sum = path_sum * 2 + root.val

        if root.left is None and root.right is None:
            return path_sum

        l_sum = sum_paths(root.left, path_sum)
        r_sum = sum_paths(root.right, path_sum)

        return l_sum + r_sum

    path_sum = sum_paths(root, 0)
    return path_sum


############################################################
# 13. sum the root to leaf path - recursive
def sum_root_to_leaf_recursive(root):
    path_sum = 0
    if root is None:
        return 0

    def sum_paths(root, path_sum):
        if root is None:
            return 0
        path_sum = path_sum * 10 + root.val

        if root.left is None and root.right is None:
            return path_sum

        l_sum = sum_paths(root.left, path_sum)
        r_sum = sum_paths(root.right, path_sum)

        return l_sum + r_sum

    path_sum = sum_paths(root, 0)
    return path_sum


############################################################
# 14. path with given sum - recursive
def given_sum_path(root, path_sum):
    if root is None:
        return None

    def find_path(root, path_sum):
        if root is None:
            return False

        path_sum = path_sum - root.val
        if root.left is None and root.right is None and path_sum == 0:
            return True

        l_path = find_path(root.left, path_sum)
        r_path = find_path(root.right, path_sum)

        return l_path or r_path

    is_path = find_path(root, path_sum)
    return is_path


############################################################
# 15. path with given sum also return path - recursive
def given_sum_path_with_path(root, path_sum):
    if root is None:
        return None
    temp_path = []
    path_list = []

    def find_path(root, path_sum, temp_path, path_list):
        if root is None:
            return path_list

        path_sum = path_sum - root.val
        temp_path.append(root.val)
        if root.left is None and root.right is None and path_sum == 0:
            path_list.append(temp_path.copy())

        find_path(root.left, path_sum, temp_path, path_list)
        find_path(root.right, path_sum, temp_path, path_list)
        temp_path.pop()

    find_path(root, path_sum, temp_path, path_list)
    return path_list



############################################################
def main():
    print('test')
    # inorder_traversal(root)

    # preorder_traversal(root)

    # postorder_traversal(root)

    # h = height_of_tree(root)
    # print(h)

    # is_h_b = is_height_balanced(root)
    # print(is_h_b)

    # is_sym = is_symmetric(root)
    # print(is_sym)

    # path_list = all_paths_from_root_to_leaf(root)
    # print(path_list)

    # n = 4
    # path = path_from_root_to_given_leaf(root, n)
    # print(path)

    # n1 = 5
    # n2  = 3
    # lca = lowest_common_ancestor(root, n1, n2)
    # print(lca)

    # n1 = 5
    # n2 = 3
    # lca = lca_recursivee(root, n1, n2)
    # print(lca.val)

    # sum = sum_root_to_leaf_binary(root)
    # print(sum)

    # sum = sum_root_to_leaf_binary_recursive(root)
    # print(sum)

    # sum = sum_root_to_leaf_recursive(root)
    # print(sum)

    # is_path = given_sum_path(root, 7)
    # print(is_path)

    path_list = given_sum_path_with_path(root, 9)
    print(path_list)

if __name__ == '__main__':
    main()

