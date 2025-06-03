def leap_year_calculation(year):
    print("\n")
    # set range within +- 2 years
    for i in range(year-2, year+3):
        # handle output if the year is leap year
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            if (year - i) > 0:
                print(f"{year - i} year(s) ago, {i}, IS a leap year")
            elif year == i:
                print(f"This year, {i}, IS a leap year")
            else:
                print(f"{i - year} year(s) later, {i}, IS a leap year")
        # handle output if not a leap year 
        else:
            if (year - i) > 0:
                print(f"{year - i} year(s) ago, {i}, is NOT a leap year")
            elif year == i:
                print(f"This year, {i}, is NOT a leap year")
            else:
                print(f"{i - year} year(s) later, {i}, is NOT a leap year")
            