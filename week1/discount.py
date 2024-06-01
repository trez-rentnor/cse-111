"""
CSE 111 Week 1 Personal Assignment

Author: Randy Jones
"""

from datetime import datetime

TUESDAY = 2
WEDNESDAY = 3

day_of_week = datetime.today().weekday()
day_of_week = TUESDAY

while True:
    subtotal = float(input("What is the subtotal? "))

    if subtotal == 0:
        print("Finished, Done, Kaput")
        exit()

    else:
        if day_of_week == TUESDAY or day_of_week == WEDNESDAY:
            if subtotal > 50.0:
                discount = subtotal * 0.1
                subtotal -= discount
                print(f"Applying discount of ${discount:.2f}")
            else:
                amount_needed = 50.0 - subtotal
                print(f"To receive discount spend an additional ${amount_needed:.2f}")

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Applying sales tax of ${sales_tax:.2f}")
        print(f"Total due: ${total:.2f}")
