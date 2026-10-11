weather = input("Enter the current weather condition: ")
homework = input("Do you finish the homework? (yes/no): ")
day = input("Please enter the day of the week: ")
if weather == "sunny" and homework == "yes":
    print("After school: Go head to the park and play!")
if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella!")
if not (homework == "yes"):
    print("Homework: Hurry up and finish your homework first!")
if day != "Saturday" and day != "Sunday":
    print("It's a school week day")