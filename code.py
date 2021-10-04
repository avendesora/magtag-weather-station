# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
from adafruit_magtag.magtag import MagTag

magtag = MagTag()

# magtag.add_text(
#    text_position=(
#        50,
#        (magtag.graphics.display.height // 2) - 1,
#    ),
#    text_scale=3,
# )

# magtag.set_text("Hello World")

# button_colors = ((255, 0, 0), (255, 150, 0), (0, 255, 255), (180, 0, 255))
# button_tones = (1047, 1318, 1568, 2093)

while True:
    for i, b in enumerate(magtag.peripherals.buttons):
        if not b.value:
            if i == 0:
                print("Hi!")
            elif i == 1:
                print("Blah!")
            elif i == 2:
                print("Wowzers!")
            elif i == 3:
                print("Bye!")

            # magtag.peripherals.neopixel_disable = False
            # magtag.peripherals.neopixels.fill(button_colors[i])
            break
    else:
        # magtag.peripherals.neopixel_disable = True
        # magtag.peripherals.neopixels.fill((0, 0, 0))
        ...

    time.sleep(0.01)
