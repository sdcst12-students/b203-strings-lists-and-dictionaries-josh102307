items = {
    "weapon": "knife",
    "heal": "bandage",
    "armour": "chestplate",
    "defense": "sheild",
}

inv = []
while True:
    print("=================================")
    print("get item, remove item, see inv")
    print("=================================")
    x = input("input: ")
    if x == 'get item':
        print(items)
        get = input("choose an item: ")
        if get == 'knife' or 'bandage' or 'chestplate' or 'sheild':
            inv.append(get)
            print(f"inventory: {inv}")
            

    if x == 'remove item':
        print(f"inventory: {inv}")
        remove = input("choose an item to remove: ")
        a = inv.index(remove)
        inv.pop(a)
        print(f"inventory: {inv}")
        for i in inv:
            if inv.count(i) >1:
                inv.remove(i)
                print(f"inventory: {inv}")




    if x == 'see inv':
        print(f"inventory: {inv}")


    

        

        


    
        
        
        
        
