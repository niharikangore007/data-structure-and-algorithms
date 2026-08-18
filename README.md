 Non-Recursive Inorder Tree Traversal (Employee Management System)

A lightweight Python program that takes employee IDs from user input, constructs a Binary Search Tree (BST), and displays them in sorted order—without recursion.

 Why I Built This

Recursive functions risk crashing with a `RecursionError` when handling large or deeply skewed trees. To prevent stack overflow issues, this project uses an non-recursive)** approach with a manual to handle tree traversal safely.



How It Works

1. User Input:** Takes space-separated Employee IDs and inserts them into a Binary Search Tree.
2. Inorder Traversal:** Visits nodes in Left root right order.
3. Explicit Stack:Instead of relying on Python's recursion stack, a standard list acts as a **LIFO (Last In, First Out)** stack:
   * Keeps moving left, pushing nodes onto the stack.
   * Pops and prints the node when a left dead-end is reached.
   * Transitions to the right child and repeats.


