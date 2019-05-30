class Time:
    """Repersents the time of day.

    attributes: hour, minute, second
    """

def print_time(t):
    print('%.2d : %.2d : %.2d', t.hour,)


time = Time()
time.hour = 11
time.minute = 59
time.second = 30
