# This program is to test the LinkedList class

from DataStructures.linkedlist.linkedlist_class import LinkedList


def main():
    ll = LinkedList()

    # Insert 10 nodes in linked list
    print('linked list with 10 elements')
    for i in range(10):
        ll.insert_node_at_end(i)
    ll.print_list()

    # delete three nodes at the end in the linked list
    print('\ndelete last three elements')
    for i in range(3):
        ll.delete_node_at_end()
    ll.print_list()

    # insert a node at the Head
    print('\ninsert a node at head')
    ll.insert_node_at_head(10)
    ll.print_list()

    # delete a node at the Head
    print('\ndelete a node from head')
    ll.delete_node_at_head()
    ll.print_list()

    # Insert a node 20 after node 2
    print('\ninsert a node after a given node')
    ll.insert_node_after_give_node(20, 2)
    ll.print_list()

    # delete the node 20
    print('\ndelete a given node')
    ll.delete_given_node(20)
    ll.print_list()

    # search for node 4 in the linked list
    print('\nsearch for a node in linked list')
    ll.search_node(4)

    # sum all elements of the linked list
    print('\nsum all elements of a linked list')
    elem_sum = ll.sum_all_elements()
    print('Sum of the linked list: {}'.format(elem_sum))

    # count the number of nodes in the linked list
    print('\ncount the number of elements of a linked list')
    num_nodes = ll.count_nodes()
    print('Total number of nodes in linked list: {}'.format(num_nodes))

    # reverse a linked list
    print('\nreverse a linked list')
    ll.reverse_list()
    ll.print_list()


if __name__ == '__main__':
    main()


