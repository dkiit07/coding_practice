# Singly Linked List
#
# Functions Implemented
#
# 1. Print linked list
# 2. Insert Node
#    a. At the End
#    b. At the Head
#    c. After the given node
# 3. Delete Node
#    a. At the end
#    b. At the Head
#    c. After the given node
# 4. Search an element
# 5. Sum all elements
# 6. Count number of nodes
# 7. Reverse the list


# Node Class
class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


# Linked List class with head as Instance Attribute
class LinkedList:

    def __init__(self, head=None):
        self.head = head

    # Insert Node method
    # Insert the new node at the tail of the linked list
    def insert_node_at_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next_node is not None:
                temp_node = temp_node.next_node
            temp_node.next_node = new_node

    # Insert the new node at the head of the linked list
    def insert_node_at_head(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # Insert after a perticular value
    def insert_node_after_give_node(self, val, given_val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.val is not given_val:
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

    # Print Linked List method
    # prints the list from head to tail
    def print_list(self):
        temp_node = self.head

        while temp_node.next_node is not None:
            print(temp_node.val, ' -> ', end='')
            temp_node = temp_node.next_node
        print(temp_node.val)

    # Delete node method
    # delete the node at the end of linked list
    def delete_node_at_end(self):
        temp_node = self.head
        while temp_node.next_node.next_node is not None:
            temp_node = temp_node.next_node
        to_delete = temp_node.next_node
        temp_node.next_node = None
        del to_delete

    # delete the node at the head of the linked list
    def delete_node_at_head(self):
        temp_node = self.head
        self.head = temp_node.next_node
        del temp_node

    # delete the given node
    def delete_given_node(self, given_val):
        temp_node = self.head
        while temp_node.next_node.val is not given_val:
            temp_node = temp_node.next_node
        to_delete = temp_node.next_node
        temp_node.next_node = temp_node.next_node.next_node
        del to_delete

    # Search for a node with the given value
    def search_node(self, given_val):

        if self.head is None:
            print('Empty List')
        else:
            temp_node = self.head
            while temp_node is not None and temp_node.val is not given_val:
                temp_node = temp_node.next_node
            if temp_node is not None:
                print('Value {} found in list'.format(given_val))
            else:
                print('Value {} not found in list'.format(given_val))

    # Sum of all elements of the linked list
    def sum_all_elements(self):
        elem_sum = 0
        if self.head is None:
            return elem_sum
        else:
            temp_node = self.head
            while temp_node is not None:
                elem_sum += temp_node.val
                temp_node = temp_node.next_node
        return elem_sum

    # Count Number of nodes in the linked list
    def count_nodes(self):
        num_nodes = 0
        if self.head is None:
            return num_nodes
        else:
            temp_node = self.head
            while temp_node is not None:
                temp_node = temp_node.next_node
                num_nodes += 1
        return num_nodes

    # Reverse a linked list
    def reverse_list(self):
        if self.head is None or self.head.next_node is None:
            pass
        else:
            prev_node = self.head
            temp_node = self.head.next_node
            fwd_node = self.head.next_node.next_node

            prev_node.next_node = None
            while temp_node is not None:
                temp_node.next_node = prev_node
                prev_node = temp_node
                temp_node = fwd_node
                if temp_node is not None:
                    fwd_node = temp_node.next_node
            self.head = prev_node
