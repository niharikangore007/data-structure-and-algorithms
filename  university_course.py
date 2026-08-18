class Node:
    def __init__(self, course_code):
        self.course_code = course_code
        self.left = None
        self.right = None

def insert(root, course_code):
    if not root:
        return Node(course_code)
    if course_code < root.course_code:
        root.left = insert(root.left, course_code)
    elif course_code > root.course_code:
        root.right = insert(root.right, course_code)
    return root

# 1. Recursive Inorder Traversal
def recursive_inorder(root):
    if root:
        recursive_inorder(root.left)
        print(root.course_code, end=" ")
        recursive_inorder(root.right)

# 2. Non-Recursive (Iterative) Inorder Traversal using a Stack
def non_recursive_inorder(root):
    stack = []
    current = root
    
    while current or stack:
        # Step 1: Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left
            
        # Step 2: Pop and process the node
        current = stack.pop()
        print(current.course_code, end=" ")
        
        # Step 3: Shift to the right child
        current = current.right


root = None
user_input = input("Enter Course Codes separated by space (e.g. CS103 CS101 CS105 CS102): ")
courses = user_input.split()

for course in courses:
    root = insert(root, course)

print("\nRecursive Inorder Traversal ")
recursive_inorder(root)

print("\n\nNon-Recursive Inorder Traversal ")
non_recursive_inorder(root)
print()