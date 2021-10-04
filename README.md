# MagTag Clock and Weather Station

This is an in (early stages) progress project to integrate an [AdaFruit MagTag](https://learn.adafruit.com/adafruit-magtag) with an analog wall clock to display indoor/outdoor temperature and humidity, indoor air quality, weather forecast, and maybe some other stuff.

Pressing different buttons on the MagTag will display different information.

Here are some articles/tutorials/guides that we might end up using for instruction and inspiration:

* [Hello World](https://learn.adafruit.com/creating-magtag-projects-with-circuitpython)
* [Cat Feeder Clock](https://learn.adafruit.com/magtag-cat-feeder-clock)
* [Showerthoughts and Quotes](https://learn.adafruit.com/magtag-showerthoughts)
* [Slideshow](https://learn.adafruit.com/magtag-slideshow)
* [Language Flashcards](https://learn.adafruit.com/magtag-flashcards)
* [AdaBox 017](https://learn.adafruit.com/adabox017)
* [Daily Weather Forecast Display](https://learn.adafruit.com/magtag-weather)
* [Displaying Temperature and Humidity](https://blog.adafruit.com/2020/12/04/displaying-temperature-and-humidity-with-an-adafruit-magtag-eink-display-circuitpython-magtag-adafuit-jonnybergdahl/)

## Requirements

The following hardware and software are required for this project.

### Hardware

TODO

### Software

In addition to the code in this repository, the following software is required.

#### CircuitPython

We're using CircuitPython on an AdaFruit MagTag. For information on how to get CircuitPython installed and ready-to-use on the MagTag, follow the instructions in the [AdaFruit MagTag guide](https://blog.adafruit.com/2020/12/04/displaying-temperature-and-humidity-with-an-adafruit-magtag-eink-display-circuitpython-magtag-adafuit-jonnybergdahl/) up through the "Welcome to CircuitPython" steps.

#### CircuitPython Libraries

There are many optional libraries available for CircuitPython. They are all available at [https://circuitpython.org/libraries](https://circuitpython.org/libraries).

The following CircuitPython libraries are required by this project:

##### Folders

* adafruit_bitmap_font
* adafruit_display_text
* adafruit_io
* adafruit_magtag
* adafruit_portalbase

##### Files

* adafruit_fakerequests.mpy
* adafruit_miniqr.mpy
* adafruit_requests.mpy
* neopixel.mpy
* simpleio.mpy
