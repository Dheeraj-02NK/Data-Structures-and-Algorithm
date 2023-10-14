class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert the element to the beginning of the Linked List
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    # Insert the element to the end of the Linked List
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    # Print the Linked List
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()

    while True:
        choice = int(input("\n\n1. Insert at Beginning\n2. Insert at End\n3. Terminate\nEnter your choice: "))
        if choice == 1:
            data = int(input("Enter the data: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            ll.insert_at_end(data)
        elif choice == 3:
            print("\nTerminated !!")
            break
        else:
            print("invalid input!!")
    print("Linked List:")
    ll.print()