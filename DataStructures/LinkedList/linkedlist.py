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
# 8. Concatenate two lists
# 9. Merge two sorted lists


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

    # concatenate two linked lists
    def concat_lists(self, head1, head2):
        temp_node = head1
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node
        temp_node.next_node = head2



def main():
    ll = LinkedList()

    # Insert 10 nodes in linked list
    for i in range(10):
        ll.insert_node_at_end(i)
    ll.print_list()

    # delete three nodes at the end in the linked list
    for i in range(3):
        ll.delete_node_at_end()
    ll.print_list()

    # insert a node at the Head
    ll.insert_node_at_head(10)
    ll.print_list()

    # delete a node at the Head
    ll.delete_node_at_head()
    ll.print_list()

    # Insert a node 20 after node 2
    ll.insert_node_after_give_node(20, 2)
    ll.print_list()

    # delete the node 20
    ll.delete_given_node(20)
    ll.print_list()

    # search for node 4 in the linked list
    ll.search_node(4)

    # sum all elements of the linked list
    elem_sum = ll.sum_all_elements()
    print('Sum of the linked list: {}'.format(elem_sum))

    # count the number of nodes in the linked list
    num_nodes = ll.count_nodes()
    print('Total number of nodes in linked list: {}'.format(num_nodes))

    # reverse a linked list
    ll.reverse_list()
    ll.print_list()

    # create two lists and concat
    ll1 = LinkedList()
    for i in range(5):
        ll1.insert_node_at_end(i)
    ll1.print_list()

    ll2 = LinkedList()
    for i in range(5):
        ll2.insert_node_at_end(i+10)
    ll2.print_list()

    ll1.concat_lists(ll1.head, ll2.head)
    ll1.print_list()


if __name__ == '__main__':
    main()


