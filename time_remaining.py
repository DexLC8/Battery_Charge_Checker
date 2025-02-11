import math
charge = input("What is your charge in Amp hours? ")
usage = input("What is your average usage in Amps? ")
charge = float(charge)
usage = float(usage)
hours = charge / usage
round_hours = math.floor(hours)
minutes = hours - round_hours
minutes = minutes * 60
round_minutes = math.floor(minutes)
seconds = minutes - round_minutes
seconds = seconds * 60
round_seconds = math.floor(seconds)
print("Your battery time remaining is:", round_hours, "hours,", round_minutes, "minutes, and", round_seconds, "seconds.")