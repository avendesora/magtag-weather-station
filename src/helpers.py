def format_time(time_struct, twelve_hour=True):
    """Given a time.struct_time, return a string as H:MM or HH:MM, either
    12- or 24-hour style depending on twelve_hour flag.
    """
    postfix = ""
    hour = time_struct.tm_hour

    if twelve_hour:
        postfix = "am" if hour < 12 else "pm"
        hour = 12 if hour == 0 else hour if hour <= 12 else hour - 12

    return f"{hour:02d}:{time_struct.tm_min:02d}{postfix}"
