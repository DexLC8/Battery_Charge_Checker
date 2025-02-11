capacity = input("What is your total battery capacity in Amp hours? ")
charge = input("What is your current SoC in Amp hours? ")
capacity = float(capacity)
charge = float(charge)
percentage = charge / capacity
percentage = percentage * 100
print("Your percentage is,", percentage, "percent.")