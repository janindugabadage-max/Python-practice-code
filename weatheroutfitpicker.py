temperature = float(input("Enter the current temperature in Celsius: "))
if temperature < 20:
    outfit = "jacket"
    print("It's cold today!")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It's warm today!")
    print("Wear a", outfit)
is_raining = input("Is it raining? (yes/no): ")
if is_raining == "yes":
    print("Bring an umbrella!")
wind_speed = float(input("Enter the wind speed in km/h: "))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It's windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("It's calm today.")
    print("No windbreaker needed over your", outfit)
has_puddles = input("Are there puddles on the ground? (yes/no): ")
if has_puddles == "yes":
    shoes = "boots"
    print("the ground is wet.")
    print("Wear ", shoes)
else:
    shoes = "sneakers"
    print("the ground is dry.")
    print("Wear ", shoes)

print("")
print("weather check is complete.")

print("=====Weather Outfit Picker=====")
print("Temperature:", temperature)
print("outfit chosen:", outfit)
print("Raining:", is_raining)
print("wind breaker needed:", needs_windbreaker)
print("Shoes chosen:", shoes)
print("===================")