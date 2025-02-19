def days_since_birthday(birthday, current_date):
    """
    Calculates the number of days since birthday, counting only whole years.
    Excludes the birth year and the current year.
    Accounts for leap years.
    :param birthday: String in the format "DD-MM-YYYY"
    :param current_date: String in the format "DD-MM-YYYY"
    :return: Number of days
    """
    # Extract years from the input strings
    birth_year = int(birthday[-4:])
    current_year = int(current_date[-4:])

    # If there are no full years in between, return 0
    if current_year - birth_year <= 1:
        return 0

    # Helper function to check for leap year
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Count full years between birth year + 1 and current year - 1
    total_days = 0
    for year in range(birth_year + 1, current_year):
        if is_leap_year(year):
            total_days += 366
        else:
            total_days += 365

    return total_days


# User input section with validation
current_date = input("Enter the current date in the format DD-MM-YYYY: ")

while True:
    birthday = input("Enter your birthday in the format DD-MM-YYYY: ")

    # Extract year, month, and day from inputs for validation
    birth_day = int(birthday[:2])
    birth_month = int(birthday[3:5])
    birth_year = int(birthday[-4:])

    current_day = int(current_date[:2])
    current_month = int(current_date[3:5])
    current_year = int(current_date[-4:])

    # Validate that the birthday is not later than the current date
    if (birth_year > current_year or
            (birth_year == current_year and birth_month > current_month) or
            (birth_year == current_year and birth_month == current_month and birth_day > current_day)):
        print("Birthday is later than the current date. Please enter a valid past birthday.")
    else:
        break  # Valid birthday entered, exit loop

# Calculate the result and print it
result = days_since_birthday(birthday, current_date)
print(f"Whole days from full years since {birthday} until {current_date}: {result}")


