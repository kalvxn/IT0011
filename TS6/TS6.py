class Item:
    def __init__(self, item_id, name, description, price):
        if not item_id.isalnum():
            raise ValueError("ID must be alphanumeric.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if not description.strip():
            raise ValueError("Description cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        try:
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print(f"Item '{name}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def read_items(self):
        if not self.items:
            print("No items available.")
            return
        for item in self.items.values():
            print(f"ID: {item.id}, Name: {item.name}, Description: {item.description}, Price: ₱{item.price}")

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Item not found.")
            return
        item = self.items[item_id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price and price > 0:
            item.price = price
        print(f"Item '{item_id}' updated successfully.")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item '{item_id}' deleted successfully.")
        else:
            print("Item not found.")

def main():
    manager = ItemManager()

    while True:
        print("\n1. Add Item\n2. View Items\n3. Update Item\n4. Delete Item\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter name: ")
                description = input("Enter description: ")
                price = float(input("Enter price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Price must be a number.")

        elif choice == "2":
            manager.read_items()

        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            name = input("Enter new name (leave empty to keep unchanged): ")
            description = input("Enter new description (leave empty to keep unchanged): ")
            try:
                price_input = input("Enter new price (leave empty to keep unchanged): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Price must be a number.")

        elif choice == "4":
            item_id = input("Enter item ID to delete: ")
            manager.delete_item(item_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
