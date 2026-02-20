#day = input("what day of the week is it:")

#if day == 'saturday' or day == 'sunday':
#    print("it's the weekend")
#else:
#    print("ugh it's a workday :(")

#if age < 5 or age >= 65:
#    print("you get in for free!")
#else:
#    print("that will; be $5")

day = "Tuesday"
is_vet = False
age = 56
#Veterens get in free on tuesdays
#Infants under 2 get in for free always

#if age <= 2 or is_vet and day == "Tuesday":
#    print("YOU GET IN FOR FREE TODAY!")

if not age <= 2 or is_vet and day == "Tuesday":
    print("YOU HAVE TO BUY A TICKET!")