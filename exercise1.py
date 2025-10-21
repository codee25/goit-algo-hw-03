from datetime import datetime, date


def get_days_from_today(date_str):
    given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    today_date = date.today()
    time_difference = today_date - given_date
    return time_difference.days


print(get_days_from_today('2020-10-09'))
