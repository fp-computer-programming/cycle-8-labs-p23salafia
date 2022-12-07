#JS 12/2/2022 Lab 8-2
#Define Guests
guest1 = input("Who is the first guest :")
guest2 = input("Who is the second guest :")
guest3 = input("Who is the third guest :")
guest_list = guest1, guest2, guest3

#Loop and function that prints every time loop runs
for x in guest_list:
    print("Hi " + x + "! You're invited to my party on Friday!")