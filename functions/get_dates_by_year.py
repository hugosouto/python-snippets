from datetime import datetime

def get_date_list(start_year, end_year=None):
    """
    Returns a list of days in the format year-month-day based on the input starting year and optional end year.
    If the end year is not passed, the current year is used.
    """
    current_year = datetime.now().year
    end_year = end_year or current_year
    date_list = []
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            if month == 2:
                if year % 4 == 0:
                    days = range(1, 30)
                else:
                    days = range(1, 29)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                days = range(1, 31)
            else:
                days = range(1, 32)
            for day in days:
                date_list.append(f"{year}-{month:02d}-{day:02d}")
    return print(date_list)

get_date_list(2015)