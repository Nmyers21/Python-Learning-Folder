unit = input("What unit are you using? ")
temp = int(input("What termperature is the water? "))

if unit == 'f':
    if temp == 212:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING. MUST HIT 212F")
elif unit == 'c':
    if temp == 100:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING. MUST HIT 100c")
elif unit == 'k':
    if temp == 373:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING. MUST HIT 373k")
else:
    print("I don't know those units, sorry!")

#f - 212
#c - 100
#k - 373
