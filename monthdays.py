month=input("enter the month:")
if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
    print("31 days")
elif month=="february":
    print("28 days or 29 days in leap year")
elif month=="april" or month=="june" or month=="september" or month=="november":
    print("30 days")
else:
    print("invalid input")