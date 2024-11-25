class ContactNode:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.left = None
        self.right = None

class ContactBookBST:
    def __init__(self):
        self.root = None

    def insert_contact(self, name, phone_number):
        if self.root is None:
            self.root = ContactNode(name, phone_number)
        else:
            self._insert(self.root, name, phone_number)

    def _insert(self, current_node, name, phone_number):
        if name < current_node.name:
            if current_node.left is None:
                current_node.left = ContactNode(name, phone_number)
            else:
                self._insert(current_node.left, name, phone_number)
        elif name > current_node.name:
            if current_node.right is None:
                current_node.right = ContactNode(name, phone_number)
            else:
                self._insert(current_node.right, name, phone_number)
        else:
            print(f"Contact with name '{name}' already exists.")

    def search_contact(self, name):
        return self._search(self.root, name)

    def _search(self, current_node, name):
        if current_node is None:
            return "Contact not found."
        elif current_node.name == name:
            return f"Name: {current_node.name}, Phone Number: {current_node.phone_number}"
        elif name < current_node.name:
            return self._search(current_node.left, name)
        else:
            return self._search(current_node.right, name)

    def delete_contact(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, current_node, name):
        if current_node is None:
            return current_node
        if name < current_node.name:
            current_node.left = self._delete(current_node.left, name)
        elif name > current_node.name:
            current_node.right = self._delete(current_node.right, name)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node with two children
            temp = self._min_value_node(current_node.right)
            current_node.name = temp.name
            current_node.phone_number = temp.phone_number
            current_node.right = self._delete(current_node.right, temp.name)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display_contacts(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, current_node):
        if current_node:
            self._in_order_traversal(current_node.left)
            print(f"Name: {current_node.name}, Phone Number: {current_node.phone_number}")
            self._in_order_traversal(current_node.right)

# Example usage
contact_book = ContactBookBST()
contact_book.insert_contact("Alice", "123-456-7890")
contact_book.insert_contact("Bob", "234-567-8901")
contact_book.insert_contact("Charlie", "345-678-9012")

print(contact_book.search_contact("Alice"))  

contact_book.delete_contact("Bob")
contact_book.display_contacts()
