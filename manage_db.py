import connection as collection
import csv
from datetime import datetime


def clear_db():
    collection.beverages.delete_many({})
    collection.equipments.delete_many({})
    collection.bills.delete_many({})
    collection.customers.delete_many({})
    collection.discounts.delete_many({})

def add_data_to_db():
    with open("./data/beverages.csv") as beverages_data:
        data = csv.reader(beverages_data, delimiter=",")
        for row in data:
            beverage = {
                "name": row[0],
                "description": row[1],
                "price": int(row[2]),
            }
            print(beverage)
            collection.beverages.insert_one(beverage)

    with open("./data/equipments.csv") as equipment_data:
        data = csv.reader(equipment_data, delimiter=",")
        for row in data:
            equipment = {
                "name": row[0],
                "amount": row[1],
                "price": int(row[2]),
            }
            print(equipment)
            collection.equipments.insert_one(equipment)

    with open("./data/customers.csv") as customer_data:
        data = csv.reader(customer_data, delimiter=",")

        for row in data:
            customer = {
                "First Name": row[0],
                "Last Name": row[1],
                "Gender": row[2],
                "Age": int(row[3])
            }
            collection.customers.insert_one(customer)

    with open("./data/bills.csv") as bill_data:
        data = csv.reader(bill_data, delimiter=",")

        for row in data:
            order_name = f"{row[0]} {row[1]}"
            orders = row[2].split(",")
            total_price = 0
            dt_object = datetime.fromtimestamp(int(row[3]))
            bill = {
                "Order Name": order_name,
                "Orders": orders,
                "Total price": total_price,
                "Date": dt_object,
            }
            collection.bills.insert_one(bill)
# clear_db()
# add_data_to_db()