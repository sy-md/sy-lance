import json
import questionary
from datetime import datetime
from pathlib import Path

class InventoryManager:
    def __init__(self, file_path="inventory.json"):
        self.file_path = file_path
        self.inventory = self.load_inventory()
        self.backup_file = f"inventory_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    def load_inventory(self) -> dict:
        """Load inventory data from JSON file with error handling."""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: File '{self.file_path}' contains invalid JSON.")
            raise

    def save_backup(self):
        """Create a backup before making changes."""
        with open(self.backup_file, 'w') as f:
            json.dump(self.inventory, f, indent=2)
        print(f"Backup saved to {self.backup_file}")

    def save_inventory(self):
        """Save updated inventory to JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(self.inventory, f, indent=2)

    def get_valid_items(self) -> list:
        """Get list of valid item names, excluding unnamed entries."""
        return [name for name in self.inventory 
                if not str(name).startswith("Unnamed:") and name != "null"]

    def select_items(self) -> list:
        """Fuzzy-select items from inventory with multi-select support."""
        item_names = self.get_valid_items()
        return questionary.checkbox(
            "🔍 Search and select items (type to fuzzy match, SPACE to select):",
            choices=item_names,
            style=questionary.Style([
                ('selected', 'fg:#ff0000 bold'),
                ('highlighted', 'bg:#ff0000 fg:#000000')
            ])
        ).ask()

    def update_item_usage(self, item_name: str):
        """Update item quantity with validation and difference calculation."""
        if item_name not in self.inventory:
            print(f"⚠️ Error: '{item_name}' not found in inventory.")
            return False

        item_data = self.inventory[item_name]
        item_id = next(iter(item_data))
        current_values = item_data[item_id]
        current_qty = current_values[-1] if current_values else 0

        while True:
            new_qty = questionary.text(
                f"Current '{item_name}': {current_qty}\n"
                "How many are ACTUALLY available now?",
                validate=lambda val: val.lstrip('-').isdigit() if val else False,
                default=str(current_qty)
            ).ask()

            if not new_qty:
                return False

            new_qty = int(new_qty)
            difference = new_qty - current_qty
            
            confirm = questionary.confirm(
                f"Update '{item_name}' from {current_qty} to {new_qty} (Δ: {difference})?"
            ).ask()
            
            if confirm:
                item_data[item_id].append(new_qty)
                print(f"✅ Updated '{item_name}': {current_qty} → {new_qty}")
                return True
            else:
                retry = questionary.confirm("Enter different quantity?").ask()
                if not retry:
                    return False

    def show_summary(self, selected_items: list):
        """Display summary of changes."""
        print("\n📝 Update Summary:")
        for item in selected_items:
            if item in self.inventory:
                item_id = next(iter(self.inventory[item]))
                history = self.inventory[item][item_id]
                if len(history) >= 2:
                    change = history[-1] - history[-2]
                    print(f"{item}: {history[-2]} → {history[-1]} (Δ: {change:+})")

    def run(self):
        """Main workflow execution."""
        print(f"\n📦 Inventory Management System")
        print(f"Loading {self.file_path}...\n")
        
        try:
            self.save_backup()
            selected_items = self.select_items()
            
            if not selected_items:
                print("No items selected. Exiting.")
                return

            updated_items = []
            for item in selected_items:
                if self.update_item_usage(item):
                    updated_items.append(item)

            if updated_items:
                self.show_summary(updated_items)
                self.save_inventory()
                print("\n💾 Inventory updated successfully!")
            else:
                print("\nNo changes were saved.")

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Using backup file. No changes were made to original inventory.")

if __name__ == "__main__":
    manager = InventoryManager()
    manager.run()
