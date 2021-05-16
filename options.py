"""
Options for program.
"""
import pymongo
import connection as collection
from datetime import datetime


def find_beverage():
    drink = input("Name: ")
    results = collection.beverages.find({"name": {"$regex" : drink.capitalize()}})
    print("\n"*3)
    print("Here are result(s)")        
    for result in results:
        print(f"Name: {result['name']:<40}    Price: {int(result['price']):>5}")


def create_bill():
    order_name = input("Order name: ")
    order_number = int(input("Order number: "))
    orders = []
    total_price = 0
    for i in range(order_number):
        beverage = input(f"{i+1}.) ")
        orders.append(beverage)
    dt_object = datetime.now()
    bill = {
                "Order Name": order_name,
                "Orders": orders,
                "Total price": total_price,
                "Date": dt_object,
        }
    print("added")
    collection.bills.insert_one(bill)


def cal_income():
    date_to_cal = input("Year-Mouth-Day: ").split("-")
    date = int(date_to_cal[2])
    income = 0 
    bills = collection.bills.find({})
    for bill in bills:
        if date == bill['Date'].day :
            income += bill['Total price']
    print(f"In {date_to_cal[0]}-{date_to_cal[1]}-{date_to_cal[2]} gains {income} ")

def cal_net_worth():
    bills = collection.bills.find({})
    equipments = collection.equipments.find({})
    incomes = 0
    expenses = 0
    for bill in bills:
        incomes += bill["Total price"]
    for e in equipments:
        expenses += e["price"]
    
    print(f"Current net worth: {incomes-expenses}")
    
def update_beverage():
    choose_beverage = input("Enter beverage name: ")
    beverage = collection.beverages.find_one({"name": choose_beverage})
    if beverage :
        name = beverage["name"]
        desc = beverage["description"]
        price = beverage["price"]
        print(f"This is current {name} value")
        print("Description")
        print(desc)
        print(f"Current price: {price}")
        update_on = input("Update on (D)escription or (P)rice or (C)ancle ?: ").lower()

        if update_on == "d":
            new_value = input("Enter a new description: ")
            update_value = {"$set": {"description": new_value }}
        elif update_on == "p":
            new_value = int(input("Enter a new price: "))
            update_value = {"$set": {"price": new_value }}
        elif update_on == "c":
            return
        else:
            print("invalid menu")
            return
        collection.beverages.update_one(beverage, update_value)
        print("Update complete!!!")
    else:
        print("cannot find beverage")

def sorting (array, keys):
    index = int(input("Which key do you want to sort")) + 1
    sort_condition = input("(A)scending, (D)escending: ").lower() 
    if sort_condition == "a" :
        sortby = pymongo.ASCENDING 

    elif sort_condition == "d" :
        sortby = pymongo.DESCENDING
    print(keys[index])
    return array.sort([(keys[1], pymongo.ASCENDING)])
    # return array.sort([(keys[index], sortby)])

def print_menu():
    print("Select")
    print("1. Find your drink")
    print("2. Calculate income per day")
    print("3. Create a new bill")
    print("4. Calculate net worth")
    print("5. Update beverage value")
    print("O to options")
    print("Q to quit")


update_beverage()