# Mini Project 2: Inventory Tracker for a Store
# Objective: Manage an inventory system where items and their prices/stock are stored and
# updated.
# Features:
# • Add new items with price and quantity.
# • Update quantity or price.
# • Show all items below a stock threshold (e.g., less than 5 units).
# • Filter items cheaper than a certain budget.
L=[]
def add_items():
    item_name=input("Enter item name:")
    for item in L:
        if item['name']==item_name:
            print("Item already exists. Use update option.\n")
            return
    item_price=float(input("Enter item price:"))
    item_quantity=int(input("Enter item quantity:"))
    L.append({'name':item_name,'price':item_price,'quantity':item_quantity})
    print("Item added successfully...")

def update_items():
    item_name=input("Enter item name to update:")
    for item in L:
        if item['name']==item_name:
            update_type=input("Choose What to update?? (1)Price (2)quantity : ")
            if update_type=='1':
                new_price=float(input("Enter updated price : "))
                if new_price:
                    item['price']=float(new_price)
                print("Price updated sucessfully.")
            elif update_type=='2':
                new_quantity=int(input("Enter updated quantity : "))
                if new_quantity:
                    item['quantity']=int(new_quantity)
                print("Quantity updated sucessfully.")
            else:
                print("Invalid option. No updates made. ")
                break
def show_lowstock():
    threshold=int(input("Enter lowstock threshold value : ") or 5)
    print(f"Items with stock less than {threshold} is : ")
    for item in L:
        if item['quantity']<threshold:
            print(f"{item['name']} - Rs{item['price']} (Qty : {item['quantity']})")
def display_items():
    for item in L:
        name=item['name']
        price=f"Rs {item['price']}"
        print(f"\n Item name : {name} \n Item price : {price} \n Item quantity : {item['quantity']}")
    print()
def main():
    while True:
        print("***WELCOME TO THE INVENTORY***")
        print("1.Add item")
        print("2.Update item")
        print("3.Show low stock")
        print("4.Show inventory")
        print("5.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            add_items()
        elif choice=="2":
            update_items()
        elif choice=="3":
            show_lowstock()
        elif choice=="4":
            display_items()
        else:
            print("Exiting...")
            break
main()