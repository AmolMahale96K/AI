import calendar

def display_calendar(year, month):
    # Display the calendar for the specified month and year
    print(calendar.month(year, month))

# Input for year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Generate and display the calendar
display_calendar(year, month)
