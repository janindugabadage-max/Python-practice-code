print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")

age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)

if age < 4:
    age_group = "Toddler"
elif age < 12:
    age_group = "Child"
elif age < 18:
    age_group = "Teen"
else:
    age_group = "Adult"

if can_swim != "yes" and can_swim != "no":
    print("Input error: 'can swim' response must be 'yes' or 'no'.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Input error: 'adult here' response must be 'yes' or 'no'.")
    adult_known = False
else:
    adult_known = True

allowed_deep_pool = can_swim == "yes" and adult_here == "yes"

if age < 12 or can_swim == "no":
    print("Warning: Stay in the shallow end unless fully accompanied and capable.")

if adult_known and adult_here != "yes":
    print("Note: Lifeguard supervision is highly recommended since no adult is with you.")

if not swim_known or not adult_known:
    print("Verdict: Refusing to decide due to unrecognized input responses.")
elif age_group == "Toddler":
    print("Verdict: Splash pool only, always with an adult.")
elif age_group == "Child":
    print("Verdict: Main pool with an adult.")
elif age_group == "Teen":
    if can_swim == "yes":
        print("Verdict: Main pool alone.")
    else:
        print("Verdict: Main pool with an adult only.")
else:
    print("Verdict: All pools open to you.")

print()
print("Have a safe swim!")