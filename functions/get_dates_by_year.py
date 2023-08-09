from datetime import datetime

def get_date_list(start_year=1970, end_year=None, break_today=False):
    """
    Returns a list of days in the format year-month-day based on the input starting year and optional end year.
    The list stops on the actual date if break_now is True.
    
    Args:
    start_year (int): The starting year for the date range.
    end_year (int, optional): The ending year for the date range. If not provided, the current year is used.
    break_today (bool, optional): If True, the list stops on the actual date. If False, the list includes all days from the last year.
    
    Returns:
    list: A list of dates in the format year-month-day.
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
                date = datetime(year, month, day)
                if break_today and date > datetime.now():
                    break
                date_list.append(f"{year}-{month:02d}-{day:02d}")
    return date_list

print(get_date_list(2015, None, True))