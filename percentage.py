capacity = input("Total Capacity: ")
charge = input("Current SoC: ")
capacity = float(capacity)
charge = float(charge)
percentage = charge / capacity
percentage = percentage * 100
print("Your percentage is,", percentage, "percent.")