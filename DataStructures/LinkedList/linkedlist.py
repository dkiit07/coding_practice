# Singly Linked List


class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = new_node

    def print_list(self):
        temp_node = self.head

        while temp_node != None:
            print(temp_node.val, ' -> ', end='')
            temp_node = temp_node.next
        print('')


def main():
    ll = LinkedList()

    ll.insert_node(1)
    ll.print_list()

    ll.insert_node(2)
    ll.print_list()


if __name__ == '__main__':
    main()


