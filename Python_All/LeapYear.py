def is_leap(year):
    leap = False

    # Write your logic here
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print(f"{year} is_a leap year")

            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter a year"))
print(is_leap(year))