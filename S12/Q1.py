import calendar

def print_calendar(month, year):
    # Print the calendar for the given month and year
    print(calendar.month_name[month], year)
    print(calendar.monthcalendar(year, month))

# Taking user input for month and year
try:
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (e.g., 2024): "))
    
    if 1 <= month <= 12:
        print_calendar(month, year)
    else:
        print("Invalid month! Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input! Please enter valid integers for month and year.")
