inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def displayInventory(inventory):
    
    print("Inventory:")
    itemTotal = 0

    for item in list(inventory.keys()):
        itemTotal += inventory.get(item)
        print(f"{inventory.get(item)} {item}")
    
    print(f"Total number of items: {itemTotal}")


displayInventory(inventory) 