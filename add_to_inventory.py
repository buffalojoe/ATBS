inventory = {
    'rope': 1,
    'gold coin': 42,
}

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in list(inventory.keys()):
            inventory[item] += 1
        else:
            inventory[item] = 1

    print("Inventory:")
    itemTotal = 0

    for item in list(inventory.keys()):
        itemTotal += inventory.get(item)
        print(f"{inventory.get(item)} {item}")
    
    print(f"Total number of items: {itemTotal}")

addToInventory(inventory, loot)