class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    root_data = input("Enter data for the root node: ")
    root = TreeNode(root_data)

    queue = [root]

    while queue:
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for '{current_node.data}': "))
        for i in range(num_children):
            child_data = input(f"Enter data for child {i + 1} of '{current_node.data}': ")
            child_node = TreeNode(child_data)
            current_node.add_child(child_node)
            queue.append(child_node)

    return root

def print_tree(node, indent=""):
    print(indent + node.data)
    for child in node.children:
        print_tree(child, indent + "  ")

if __name__ == '__main__':
    tree = build_tree()

    while True:
        print("\nMenu:")
        print("1. Print Tree")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nTree Structure:")
            print_tree(tree)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
