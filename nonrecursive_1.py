#An organization stores employee IDs in a BST. 
# Implement non-recursive inorder traversal using a stack
#  to display the employee IDs in sorted order. 



class Node:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.left = None
        self.right = None


def insert(root, emp_id):
    if not root:
        return Node(emp_id)
    if emp_id < root.emp_id:
        root.left = insert(root.left, emp_id)
    elif emp_id > root.emp_id:
        root.right = insert(root.right, emp_id)
    return root

# Non-Recursive (Iterative) Inorder Traversal using an Explicit Stack
def non_recursive_inorder(root):
    stack = []
    current = root
    
    print("\nSorted Employee IDs:")
    while current or stack:
        # Step 1: Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left
            
        # Step 2: Pop and print the node
        current = stack.pop()
        print(current.emp_id, end=" ")
        
        # Step 3: Shift to the right child
        current = current.right
    print()


root = None
user_input = input("Enter Employee IDs separated by space (e.g. 105 101 103 102 104): ")
emp_ids = user_input.split()

for emp_id in emp_ids:
    root = insert(root, int(emp_id))

non_recursive_inorder(root)