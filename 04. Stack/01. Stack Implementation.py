# Implementation of a stack using a list
stack = []

if __name__ == '__main__':
    while True:
        print("1. Push\n2. Pop\n3. Return\n4. Terminate")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the item: "))
            stack.append(data)  # Push operation: Add an item to the stack
        elif choice == 2:
            if not stack:
                print("Stack is empty. Cannot pop.")
            else:
                popped_item = stack.pop()  # Pop operation: Remove and return the top item from the stack
                print(f"Popped item: {popped_item}")
        elif choice == 3:
            if not stack:
                print("Stack is empty. Cannot return.")
            else:
                top_item = stack[-1]  # Return operation: Return the top item from the stack without removing it
                print(f"Top item: {top_item}")
        elif choice == 4:
            print("Program terminated!!")
            break
        else:
            print("Invalid input!!")

        print("Current stack:", stack)  # Print the stack after every iteration

    print("The final stack is:", stack)
