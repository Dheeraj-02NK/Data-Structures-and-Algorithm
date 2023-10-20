class Node:
    def __init__(self, data=None, next=None):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head that is initially None
        self.head = None

    # Insert the element to the beginning of the Linked List
    def insert_at_beginning(self, data):
        # Create a new node with data and make it the new head
        node = Node(data, self.head)
        self.head = node

    # Insert the element to the end of the Linked List
    def insert_at_end(self, data):
        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            # Traverse the list to find the last node
            itr = itr.next
        # Insert the new node at the end
        itr.next = Node(data, None)

    # Get the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            # Traverse the list and count nodes
            count += 1
            itr = itr.next
        return count

    # Remove an element at the beginning
    def remove_at_begin(self):
        if self.head is None:
            print("The list is empty")
            return
        # Set the head to the next node, effectively removing the first node

    # Remove the element at the end
    def remove_at_end(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            # If there is only one element in the list, make the list empty
            self.head = None
            return
        itr = self.head
        while itr.next:
            # Traverse the list to find the second-to-last node
            self.prev = itr
            itr = itr.next
        # Remove the last node by updating the second-to-last node's next reference

    # Print the Linked List
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            # Traverse the list and build a string representation
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

# Main program
if __name__ == '__main__':
    ll = LinkedList()

    while True:
        choice = int(input("\n\n1. Insert at Beginning\n2. Insert at End\n3. Remove at beginning\n4. Remove at End\n5. Terminate\nEnter your choice: "))
        if choice == 1:
            data = int(input("Enter the data: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            ll.insert_at_end(data)
        elif choice == 3:
            ll.remove_at_begin()
        elif choice == 4:
            ll.remove_at_end()
        elif choice == 5:
            print("Terminating Program")
            break
        else:
            print("Invalid input!!")
        ll.print()
    print("\n\nFinal Linked List:")
    ll.print()
