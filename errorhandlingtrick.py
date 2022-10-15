import datetime
birthday = input("What is your birthday? (mm/dd/yyyy):")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
print("Your birth month is " + birthdate.strftime("%B"))
