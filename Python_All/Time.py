import time, datetime

Year = 2020
Month = 12
Day = 24
Hour = 23
Minute = 18
Second = 50

while True:
    Datetime = datetime.datetime(Year, Month, Day, Hour, Minute, Second)
    diff = Datetime - datetime.datetime.now()
    diff = str(diff)

    days, not_useful, time_str = diff.split()

    Day1 = days + " " + "Day" # Day

    print(Day1)

    time.sleep(1)