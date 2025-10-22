from datetime import datetime, date


def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today_date = date.today()
        time_difference = today_date - given_date
        return time_difference.days

    except ValueError:
        return f"Помилка: Неправильний формат дати '{date_str}'. Використовуйте формат 'РІК-МІСЯЦЬ-ДЕНЬ' (наприклад, '2020-10-09')."
    except Exception as e:
        return f"Виникла невідома помилка: {e}"


print(get_days_from_today('2020-10-09'))
print(get_days_from_today('13.14.2000'))
print(get_days_from_today('2025-02-30'))
