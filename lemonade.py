def greet_customer():
    print("Welcome to the Lemonade stand")
    print("Fresh Lemonade, made for you!")
greet_customer()
price_per_cup = int(input("Enter the price per cup of lemonade: "))
cups_sold = int(input("Enter the number of cups sold: "))
def calculate_total(price, cups):
    total = price * cups
    return total
total_cost = calculate_total(price_per_cup, cups_sold)
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
amount_paid = float(input("Enter the amount paid by the customer: "))
def calculate_change(paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
def thank_you_message(cups):
    if cups >= 5:
        return "Wow! Big order! Thank you for your support!"
    else:
        return "Thank you for your purchase and stopping by at our lemonade stand!"
closing_message = thank_you_message(cups_sold)
print("")
print("==== Lemonade Stand Receipt ====")
print("Price per cup: $", price_per_cup)
print("Number of cups sold: ", cups_sold)
print("Total Cost: $", rounded_total)
print("Amount Paid: $", amount_paid)
print("Change Due: $", rounded_change)
print(closing_message)
print("================================")