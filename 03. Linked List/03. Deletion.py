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

    # Get the lenght of the linked list
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    # Remove the element at a given index
    def remove_at(self, index):
        if index<0 or index>self.get_lenght() or index==self.get_lenght():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next
            return
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

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
        choice = int(input("\n\n1. Insert at Beginning\n2. Insert at End\n3. Remove at\n4. Terminate\nEnter your choice: "))
        if choice == 1:
            data = int(input("Enter the data: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            ll.insert_at_end(data)
        elif choice == 3:
            index = int(input("Enter the index: "))
            ll.remove_at(index)
        elif choice == 4:
            print("Terminating Program")
            break
        else:
            print("invalid input!!")
        ll.print()
    print("\n\nFinal Linked List:")
    ll.print()