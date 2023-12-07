class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree(node, data):
    if node is None:
        return BSTNode(data)
    if data < node.data:
        node.left = create_tree(node.left, data)
    else:
        node.right = create_tree(node.right, data)
    return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(f"\t{node.data}\t", end="")
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(f"\t{node.data}\t", end="")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(f"\t{node.data}\t", end="")

def search(node, key):
    if node is None or node.data == key:
        return node
    elif key < node.data:
        return search(node.left, key)
    else:
        return search(node.right, key)

def insert(node, key):
    if node is None:
        return BSTNode(key)
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def delete_node(node, key):
    if node is None:
        return None
    if key < node.data:
        node.left = delete_node(node.left, key)
    elif key > node.data:
        node.right = delete_node(node.right, key)
    else:
        if node.left is None and node.right is None:
            return None
        elif node.left is None:
            temp = node.right
            del node
            return temp
        elif node.right is None:
            temp = node.left
            del node
            return temp
        else:
            temp = find_min(node.right)
            node.data = temp.data
            node.right = delete_node(node.right, temp.data)
    return node

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1

if __name__ == "__main__":
    root = None

    while True:
        print("\n1.Insertion in Binary Search Tree")
        print("2.Inorder\n3.Preorder\n4.Postorder")
        print("5.Search Element in Binary Search Tree\n6.Insert in BST\n7.Delete anywhere\n8.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter N value: "))
            print("Enter the values to create BST like(6,9,5,2,8,15,24,14,7,8,5,2): ")
            values = list(map(int, input().split()))
            for data in values:
                root = create_tree(root, data)
        elif choice == 2:
            print("\nInorder Traversal: ")
            inorder(root)
        elif choice == 3:
            print("\nPreorder Traversal: ")
            preorder(root)
        elif choice == 4:
            print("\nPostorder Traversal: ")
            postorder(root)
        elif choice == 5:
            key = int(input("Enter element to be searched: "))
            n = search(root, key)
            if n is not None:
                print(f"Found: {n.data}")
            else:
                print("Not found")
        elif choice == 6:
            key = int(input("Enter element to be inserted: "))
            root = insert(root, key)
            print("Key inserted")
        elif choice == 7:
            key = int(input("Enter element to be deleted: "))
            root = delete_node(root, key)
            print(f"{key} key deleted")
        elif choice == 8:
            break
        else:
            print("Wrong input/choice")
