homework_time = int(input("Enter homework time in minutes: "))
if homework_time > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")
free_time = input("Is there free time after homework? (yes/no): ")
if free_time == "yes":
    print("Don't forget to pick a hobby!")
print("===== DAILY PLAN =====")
print("Homework Minutes: homework_time")
print("Plan: plan")
print("Free Time Answer: free_time")