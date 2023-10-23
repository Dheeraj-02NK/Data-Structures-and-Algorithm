from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)  # Use appendleft to enqueue

    def dequeue(self):
        if not self.is_empty():
            return self.container.pop()  # Use pop to dequeue
        else:
            return "Queue is empty. Cannot dequeue."

    def front(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return "Queue is empty. Nothing at the front."

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Create a Queue object
queue = Queue()

while True:
    print("Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Check if the queue is empty")
    print("5. Get the size of the queue")
    print("6. Terminate")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter the value to enqueue: "))
        queue.enqueue(val)

    elif choice == 2:
        if not queue.is_empty():
            dequeued_val = queue.dequeue()
            print(f"Dequeued value: {dequeued_val}")
        else:
            print("Queue is empty. Cannot dequeue.")

    elif choice == 3:
        if not queue.is_empty():
            front_val = queue.front()
            print(f"Front value: {front_val}")
        else:
            print("Queue is empty. Nothing at the front.")

    elif choice == 4:
        if queue.is_empty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == 5:
        print(f"Size of the queue: {queue.size()}")

    elif choice == 6:
        print("Program terminated!!")
        break
    else:
        print("Invalid choice. Try again!!!")

    # Display the current state of the queue after each iteration
    print("Current Queue:", list(queue.container))
