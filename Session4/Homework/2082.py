def add_fruit(inventory,fruit, quantity = 0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity     
    return
new_inventory = {}
add_fruit(new_inventory,"strawberries",10)
for k,v in new_inventory.items():
    print(k,v,sep=": ")

add_fruit(new_inventory,"strawberries",25)
for k,v in new_inventory.items():
    print(k,v,sep=": ")