# Singly Linked list Questions
#
# 1. Concatenate two lists
# 2. Merge two sorted lists
#

from DataStructures.linkedlist.linkedlist_class import LinkedList


# print linked list with head as parameter
def print_list_with_head(head):
    temp_node = head
    while temp_node.next_node is not None:
        print(temp_node.val, ' -> ', end='')
        temp_node = temp_node.next_node
    print(temp_node.val)


# concatenate two linked lists
def concat_lists(head1, head2):
    if head1 is None:
        return head2
    else:
        temp_node = head1
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node
        temp_node.next_node = head2
        return head1


# merge two sorted lists
def merge_sorted_lists(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    if head1.val < head2.val:
        n_h1 = head1.next_node
        n_h2 = head2
        g_head = head1
    else:
        n_h1 = head2.next_node
        n_h2 = head1
        g_head = head2
    c_node = g_head
    while n_h1 is not None and n_h2 is not None:
        if n_h1.val < n_h2.val:
            c_node.next_node = n_h1
            n_h1 = n_h1.next_node
            c_node = c_node.next_node

        else:
            c_node.next_node = n_h2
            n_h2 = n_h2.next_node
            c_node = c_node.next_node
    if n_h1 is None:
        c_node.next_node = n_h2
    else:
        c_node.next_node = n_h1

    return g_head


def main():
    # create two lists and concat
    print('Concat Linked Lists')
    ll1 = LinkedList()
    for i in range(5):
        ll1.insert_node_at_end(i)
    ll1.print_list()

    ll2 = LinkedList()
    for i in range(5):
        ll2.insert_node_at_end(i + 10)
    ll2.print_list()

    new_head = concat_lists(ll1.head, ll2.head)
    print_list_with_head(new_head)

    # merge two sorted lists
    print('\nMerge Two Sorted Linked Lists')
    ll11 = LinkedList()
    ll11.insert_node_at_end(1)
    ll11.insert_node_at_end(3)
    ll11.insert_node_at_end(6)
    ll11.print_list()

    ll22 = LinkedList()
    ll22.insert_node_at_end(0)
    ll22.insert_node_at_end(2)
    ll22.insert_node_at_end(4)
    ll22.insert_node_at_end(5)
    ll22.insert_node_at_end(7)
    ll22.print_list()

    new_head = merge_sorted_lists(ll11.head, ll22.head)
    print_list_with_head(new_head)


if __name__ == '__main__':
    main()
