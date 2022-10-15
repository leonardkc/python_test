import datetime
birthday = input("What is your birthday (mm/dd/yyyy):")
nextbirthday = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
currentdate = datetime.date.today()
difference = nextbirthday - currentdate
print(difference.days)