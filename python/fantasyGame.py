#!/usr/bin/env python3.7

# inventory

stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v.get(item, 0)
    return item_total
    print("Total number of items is: " + str(item_total))

displayInventory(stuff)
