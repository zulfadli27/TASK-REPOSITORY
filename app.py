import input_validation as iv
import leap_year as ly
import zellers_congruence as zc

# to validate user input
date, month, year = iv.input_validation()

# to determine leap year in current and +- 2 years
ly.leap_year_calculation(year)

# to define day of the week from date based on zeller's congruence algorithm
zc.calculate_date(date, month, year)