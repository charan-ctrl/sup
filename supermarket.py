from datetime import datetime

name = input("Enter your Name:")

# List of items
lists = '''
Rice       Rs 10\kg
Suger      Rs 8\kg
Oil        Rs 30\liter
Salt       Rs 25\kg
Paneer     Rs 40\kg
Maggie     Rs 12\pack
Boost      Rs 200\bottle
'''

# Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

# Rate for each item
items = {'rice': 10, 'sugar': 8, 'oil': 30, 'salt': 25, 'paneer': 40, 'maggie': 12, 'boost': 200}

while True:
    option = int(input("Press 1 for list or 2 to exit: "))
    if option == 2:
        print("Thank you for shopping")
        break
    elif option == 1:
        print(lists)

        while True:
            inp1 = int(input("To buy press 1 or press 2 to exit: "))
            if inp1 == 2:
                print("Thank you for shopping")
                break
            elif inp1 == 1:
                item = input("Choose your items: ").lower()
                quantity = int(input("Enter quantity: "))
                
                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")

        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalamount = tax + totalprice

            print(25 * "=", "Satya Supermarket", 25 * "=")
            print(28 * " ", "Hyderabad")
            print("Name:", name, 30 * "", "Date:", datetime.now())
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 8 * ' ', 5 * ' ', ilist[i], 3 * ' ', qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")



