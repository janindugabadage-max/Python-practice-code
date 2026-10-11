day = input("Please enter the day of the week:")
if day in ("Saturday", "Sunday"):
    print("Day type: Weekend - Enjoy your free time!")
elif day == "Monday":
    print("Day type: First day of the week!")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type: Midweek - Keep going!")
elif day == "Friday":
    print("Day type: Last day of the  week!")
else:
    print("Day type: Not recognized")