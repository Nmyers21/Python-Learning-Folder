firstname = input("What is your first name?")
lastname = input("What is your last name?")
total_length = len(firstname) + len(lastname)
print("*" * 20)
if total_length == 12:
    print(f"{firstname} {lastname}is Exactly Average!")
elif total_length < 12:
    print(f"{firstname} {lastname}is Shorter Than Average!")
else:
    print(f"{firstname} {lastname}is Longer than average!")

