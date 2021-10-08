import time
from adafruit_magtag.magtag import MagTag

magtag = MagTag()

magtag.add_text(
    text_position=(
        50,
        (magtag.graphics.display.height // 2) - 1,
    ),
    text_scale=3,
)

magtag.set_text("")

while True:
    for index, button in enumerate(magtag.peripherals.buttons):
        if not button.value:
            # Display Digital Time
            if index == 0:
                magtag.peripherals.neopixel_disable = False
                magtag.peripherals.neopixels.fill((255, 255, 255))
                magtag.set_text("Howdy!")

            # Display Inside Temperature and Gas Levels
            elif index == 1:
                magtag.peripherals.neopixel_disable = False
                magtag.peripherals.neopixels.fill((255, 0, 0))
                magtag.set_text("")

            # Display Outside Temperature and Forecast
            elif index == 2:
                magtag.peripherals.neopixel_disable = False
                magtag.peripherals.neopixels.fill((0, 255, 0))
                magtag.set_text("")

            # Display Random Saying
            elif index == 3:
                magtag.peripherals.neopixel_disable = False
                magtag.peripherals.neopixels.fill((0, 0, 255))
                magtag.set_text("")

            break
    else:
        magtag.peripherals.neopixel_disable = True
        magtag.peripherals.neopixels.fill((0, 0, 0))

    time.sleep(0.01)
