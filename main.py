#==========================================
# Title:  Change Program
# Author: Amir Zarei
# Date:   21 Jan 2023
#==========================================
import mathgit 

# Cents Per Dollar Constants
DOLLAR = 100
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

# Change counter function that calculate various dollar change
def change_counter(cents):
    ch = {"Dollar": math.floor(cents / DOLLAR), "Quarter": 0, "Dime": 0, "Nickel": 0, "Penny": 0}
    # calculating count for each coin
    cents = cents % DOLLAR
    ch["Quarter"] = math.floor(cents / QUARTER)
    cents = cents % QUARTER
    ch["Dime"] = math.floor(cents / DIME)
    cents = cents % DIME
    ch["Nickel"] = math.floor(cents / NICKEL)
    cents = cents % NICKEL
    ch["Penny"] = cents
    return ch


# main function
if __name__ == '__main__':
    while True:
        try:
            i = int(input('Enter total cents: '))
            if i < 0:
                break
            change = change_counter(i)
            print(
                'Dollars: ${:,} \n'
                'Quarters: {} \n'
                'Dimes: {} \n'
                'Nickels: {} \n'
                'Pennies: {}'.format(change['Dollar'],
                                     change['Quarter'],
                                     change['Dime'],
                                     change['Nickel'],
                                     change['Penny']))
        except ValueError:
            print("Error! Please enter a valid integer.")
            continue
        


