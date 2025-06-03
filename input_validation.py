def validate(message, param, min_val, max_val=None):
    # to ensure the param fit within a defined range
    while True:
        try:
            input_number = int(input(message))
            if input_number < min_val or (max_val is not None and input_number > max_val):
                print(f"{param} must be between {min_val} and {max_val}, please repeat again\n" 
                      if max_val else f"{param} must be greater than {min_val}, please repeat again\n")
            else:
                return input_number
        except ValueError:
            print("{param} must be a number")


def input_validation():
    # validate input required for main app
    date = validate("Please input the date (1-31): ","Date",1,31)
    month = validate("Please input the month (1-12): ","Month",1,12)
    year = validate("Please input the year : ","Year",1)
    return date, month, year

