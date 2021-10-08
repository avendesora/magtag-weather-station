# This was originally copied from an AdaFruit Learning System Guide (https://github.com/adafruit/Adafruit_Learning_System_Guides)
# specifically https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/MagTag_Cat_Fed_Clock/code.py
# Modifications have since been made, but the original is copyright AdaFruit and licensed under the MIT license
# (same as this code repository)
import time

from adafruit_magtag.magtag import MagTag

from constants import DAYS, MONTHS

USE_AMPM_TIME = True
last_sync = None
last_minute = None
last_day = None

magtag = MagTag()

mid_x = magtag.graphics.display.width // 2 - 1
magtag.add_text(
    text_font="/fonts/Lato-Regular-74.bdf",
    text_position=(mid_x, 5),
    text_anchor_point=(0.5, 0),
    is_data=False,
)
magtag.set_text("00:00a", auto_refresh=False)

magtag.add_text(
    text_font="/fonts/BebasNeueRegular-41.bdf",
    text_position=(mid_x, 86),
    text_anchor_point=(0.5, 0),
    is_data=False,
)
magtag.set_text("DAY 00:00a", index=1, auto_refresh=False)


def hh_mm(time_struct, twelve_hour=True):
    """Given a time.struct_time, return a string as H:MM or HH:MM, either
    12- or 24-hour style depending on twelve_hour flag.
    """
    postfix = ""
    if twelve_hour:
        if time_struct.tm_hour > 12:
            hour_string = str(time_struct.tm_hour - 12)  # 13-23 -> 1-11 (pm)
            postfix = "pm"
        elif time_struct.tm_hour > 0:
            hour_string = str(time_struct.tm_hour)  # 1-12
            postfix = "am"
            if time_struct.tm_hour == 12:
                postfix = "pm"  # 12 -> 12 (pm)
        else:
            hour_string = "12"  # 0 -> 12 (am)
            postfix = "am"
    else:
        hour_string = "{hh:02d}".format(hh=time_struct.tm_hour)
    return hour_string + ":{mm:02d}".format(mm=time_struct.tm_min) + postfix


while True:
    if not last_sync or (time.monotonic() - last_sync) > 3600:
        # at start or once an hour
        magtag.network.get_local_time()
        last_sync = time.monotonic()

    # get current time
    now = time.localtime()

    # minute updated, refresh display!
    if not last_minute or (last_minute != now.tm_min):
        magtag.set_text(hh_mm(now, USE_AMPM_TIME), index=0)
        last_minute = now.tm_min

    # day updated, refresh display!
    if not last_day or (last_day != now.tm_wday):
        weekday = DAYS[now.tm_wday][:3]
        month = MONTHS[now.tm_mon]
        out = f"{weekday}, {month} {now.tm_mday}, {now.tm_year}"
        magtag.set_text(out, index=1)
        last_day = now.tm_wday
