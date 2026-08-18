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

def inorder_traversal(root):
    stack = []
    current = root
    
    print("\nSorted Employee IDs:")
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            
        current = stack.pop()
        print(current.emp_id, end=" ")
        current = current.right
    print()

root = None
ids = input("Enter Employee IDs separated by space: ").split()

for emp_id in ids:
    root = insert(root, int(emp_id))

inorder_traversal(root)