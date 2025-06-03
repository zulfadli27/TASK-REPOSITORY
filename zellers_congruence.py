def calculate_date(date, month, year):
    try:
        # q is the day of the month
        q = date

        # m represent month, for january and february in zeller's congruence was adjusted to 13 and 14 month of the previous year
        if month == 1 or month == 2:
            m = month + 12
            year_adj = year - 1
        else:
            m = month
            year_adj = year

        # K represent the year of century, J for the zero based century
        K = year_adj % 100
        J = year_adj // 100

        # zeller's congruence formula
        h = (q + ((13*(m+1))//5) + K + (K//4) + (J//4) - 2 * J) % 7

        # converting h from number to day of the week
        if h == 0:
            day = "Saturday"
        elif h == 1:
            day = "Sunday"
        elif h == 2:
            day = "Monday"
        elif h == 3:
            day = "Tuesday"
        elif h == 4:
            day = "Wednesday"
        elif h == 5:
            day = "Thursday"
        else:
            day = "Friday"

        # to polish the output as 2 digits
        if len(str(date)) == 1:
            date = "0"+str(date)
        if len(str(month)) == 1:
            month = "0"+str(month)

        print(f"\nThe day of the week of date {date}-{month}-{year} is: {day}")

    except Exception as e:
        print(f"there is a problem, please check this message : \n{e}")
