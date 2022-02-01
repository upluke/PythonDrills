def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # SOLUTION:
    #     DAYS = [
    #     "Sunday",
    #     "Monday",
    #     "Tuesday",
    #     "Wednesday",
    #     "Thursday",
    #     "Friday",
    #     "Saturday",
    # ]

    # if day_of_week < 1 or day_of_week > 7:
    #     return None

    # return DAYS[day_of_week - 1]

    hp = {1: 'Sunday', 2: 'Tuesday', 3: 'Wednesday',
          4: 'Thursday', 5: 'Friday', 6: 'Saturaday', 7: 'Saturday'}
    return hp[day_of_week] if day_of_week >= 1 and day_of_week <= 7 else None


print(weekday_name(1))
print(weekday_name(7))
print(weekday_name(9))
print(weekday_name(0))
