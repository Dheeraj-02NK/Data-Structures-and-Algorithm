from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Create a Stack object
stack = Stack()

while True:
    print("Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if the stack is empty")
    print("5. Get the size of the stack")
    print("6. Terminate")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter the value to push: "))
        stack.push(val)

    elif choice == 2:
        if not stack.is_empty():
            popped_val = stack.pop()
            print(f"Popped value: {popped_val}")
        else:
            print("Stack is empty. Cannot pop.")

    elif choice == 3:
        if not stack.is_empty():
            top_val = stack.peek()
            print(f"Top value: {top_val}")
        else:
            print("Stack is empty. Nothing to peek.")

    elif choice == 4:
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == 5:
        print(f"Size of the stack: {stack.size()}")

    elif choice == 6:
        print("Program terminated!!")
        break
    else:
        print("Invalid choice. Try again!!!")

    # Display the current state of the stack after each iteration
    print("Current Stack:", list(stack.container))