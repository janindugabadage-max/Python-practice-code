member_name = input("Enter member name: ")
club_name = input("Enter club name: ")
member_number = 8
points = 9.5
is_active = True
badge_code = member_name[:3] + club_name[-1] + str(member_number)
print(badge_code)
print("====== CLUB BADGE ======")
print("Member: " + member_name)
print("Club: " + club_name)
print("Code: " + badge_code)
print("Points | Active: " + str(points) + " | " + str(is_active))