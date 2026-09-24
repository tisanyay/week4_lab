import json

def is_positive(num):
    return int(num) > 0

def is_digit(num):
    return num.isdigit()

def is_over_stock_limit(num):
    return int(num) > STOCK_LIMIT

def iterate_checks(list_of_checks, num):
    for check in list_of_checks:
        if not check(num):
            return False
    return True

def generate_report(units_processed, failed_entry_count):
    print("Total units processed:", units_processed)
    print("Number of failed/rejected entries:", failed_entry_count)

def get_valid_input():
    failed_entry_count = 0
    command = input("Enter stock quantity or enter 'quit': \n")

    if command == "quit":
        return 0
    
    list_of_checks = [
            is_digit,
            is_positive
        ]

    if not iterate_checks(list_of_checks, command):
        print("ERROR!!! CHECK YOUR STOCK QUANTITY AGAIN!!")
        failed_entry_count += 1

        return -1

    return int(command)

def process_delivery(current_total, new_value):
    return current_total + new_value 

def calculate_tax(amount):
    return amount * 0.1

def load_inventory(filename):
    with open(filename, "w+") as f:
        return json.load(f)

def save_inventory(data, filename):
    with open(filename, "w+") as f:
            data = json.dump(data, filename)


inventory_file = "inventory.json"
STOCK_LIMIT = 500
failed_entry_count = 0
inventory = 0
revenue = 0
price_per_qty = 10
 
print("SMART AUDITOR PROGRAM!!!!")

data = load_inventory(inventory_file)

while True:
    user_input = get_valid_input()
 
    if not user_input:
        break
    
    if user_input == -1:
        failed_entry_count += 1
        continue

    if is_over_stock_limit(inventory+user_input):
        print("ALERT: ENTRY EXCEEDS STOCK INVENTORY\nEXITING...")
        break 
    
    inventory += user_input
    raw_price = user_input * price_per_qty
    taxed_price = calculate_tax(raw_price) + raw_price
    revenue = process_delivery(revenue, taxed_price)

generate_report(inventory, failed_entry_count)
print(revenue)
