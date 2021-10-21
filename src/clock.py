# This was originally copied from an AdaFruit Learning System Guide (https://github.com/adafruit/Adafruit_Learning_System_Guides)
# specifically https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/MagTag_Cat_Fed_Clock/code.py
# Modifications have since been made, but the original is copyright AdaFruit and licensed under the MIT license
# (same as this code repository)
import time

from adafruit_magtag.magtag import MagTag

from constants import DAYS, MONTHS
from helpers import format_time


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


while True:
    if not last_sync or (time.monotonic() - last_sync) > 3600:
        # at start or once an hour
        magtag.network.get_local_time()
        last_sync = time.monotonic()

    # get current time
    now = time.localtime()

    # minute updated, refresh display!
    if not last_minute or (last_minute != now.tm_min):
        magtag.set_text(format_time(now, USE_AMPM_TIME), index=0)
        last_minute = now.tm_min

    # day updated, refresh display!
    if not last_day or (last_day != now.tm_wday):
        weekday = DAYS[now.tm_wday][:3]
        month = MONTHS[now.tm_mon]
        out = f"{weekday}, {month} {now.tm_mday}, {now.tm_year}"
        magtag.set_text(out, index=1)
        last_day = now.tm_wday
