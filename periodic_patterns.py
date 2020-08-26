import datetime

days_of_week = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]


def analyze(timestamp: datetime.datetime):
    # n-th 7-day-period of month (starts at 1)
    n = ((timestamp.day + 1) // 7) + 1

    # day of week (starts at Monday)
    dow = days_of_week[timestamp.weekday()]

    # n-th full week of month (starts at 1, can be 0)
    full_week = (timestamp.day + 6 - timestamp.weekday()) // 7

    # day fraction (0 to less than 1)
    _start = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
    _end = (timestamp + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    day_fraction = (timestamp - _start).total_seconds() / (_end - _start).total_seconds()

    # week fraction (0 to less than 1)
    week_fraction = (timestamp.weekday() + day_fraction) / 7

    # fortnight fraction
    two_week_fraction = ((datetime.timedelta(seconds=timestamp.timestamp()).days + 3) % 14 + day_fraction) / 14

    # month fraction (0 to less than 1)
    _start = timestamp.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    _end = (_start + datetime.timedelta(days=35)).replace(day=1)
    month_fraction = (timestamp - _start).total_seconds() / (_end - _start).total_seconds()

    # bimonthly fraction (0 to less than 1)
    two_month_fraction = ((timestamp.month - 1) % 2 + month_fraction) / 2

    # quarterly fraction (0 to less than 1)
    three_month_fraction = ((timestamp.month - 1) % 4 + month_fraction) / 4

    # quarterly fraction (0 to less than 1)
    six_month_fraction = ((timestamp.month - 1) % 6 + month_fraction) / 6

    # year fraction (0 to less than 1)
    _start = timestamp.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    _end = _start.replace(year=timestamp.year + 1)
    year_fraction = (timestamp - _start).total_seconds() / (_end - _start).total_seconds()

    return [n,
            dow,
            full_week,

            day_fraction,
            week_fraction,
            two_week_fraction,

            month_fraction,
            two_month_fraction,
            three_month_fraction,
            six_month_fraction,

            year_fraction,
            ]
