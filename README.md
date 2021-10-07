# MagTag Clock and Weather Station

This is an (early stages) in-progress project to integrate an [AdaFruit MagTag](https://learn.adafruit.com/adafruit-magtag) with an analog wall clock to display indoor/outdoor temperature and humidity, indoor air quality, weather forecast, and maybe some other stuff.

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

This project uses the following hardware:

* [AdaFruit MagTag](https://www.adafruit.com/product/4800) (I used the [MagTag Starter Kit](https://www.adafruit.com/product/4819), which includes magnet feet, display frames and hardware, and a lithium-ion battery in addition to the MagTag itself)
* [AdaFruit BME688](https://www.adafruit.com/product/5046) (Pressure/Humidity/Temperature/Gas Sensor)
* [AdaFruit SGP30](https://www.adafruit.com/product/3709) (Air Quality Sensor)
* [STEMMA QT cables](https://www.adafruit.com/product/4210) for connected the sensors to the MagTag (x2)
* A USB C cable and 5V 2A power supply

### Software

In addition to the code in this repository, the following software is required.

#### CircuitPython

We're using CircuitPython on an AdaFruit MagTag. For information on how to get CircuitPython installed and ready-to-use on the MagTag, follow the instructions in the [AdaFruit MagTag guide](https://blog.adafruit.com/2020/12/04/displaying-temperature-and-humidity-with-an-adafruit-magtag-eink-display-circuitpython-magtag-adafuit-jonnybergdahl/) up through the "Welcome to CircuitPython" steps.

#### CircuitPython Libraries

There are many optional libraries available for CircuitPython. They are all available at [https://circuitpython.org/libraries](https://circuitpython.org/libraries).

The following CircuitPython libraries are required by this project (just copy them into the "lib" folder on the MagTag):

##### Folders

* adafruit_bitmap_font
* adafruit_display_text
* adafruit_imageload
* adafruit_io
* adafruit_magtag
* adafruit_portalbase

##### Files

* adafruit_bme680.mpy
* adafruit_fakerequests.mpy
* adafruit_miniqr.mpy
* adafruit_requests.mpy
* adafruit_sgp30.mpy
* neopixel.mpy
* simpleio.mpy

## Configuration

This code repository includes a secrets.py file with mostly blank values for secrets that will need to be configured/populated in order for the code in code.py to work properly.

#### Network Credentials and Settings

| Secret Name | Secret Description |
| ----------- | ------------------ |
| ssid        | Your wireless network name |
| password    | Your wireless network password |

#### AdaFruit IO Credentials and Settings

This project uses io.adafruit.com to get the current date and time based on the set timezone

| Secret Name  | Secret Description |
| ------------ | ------------------ |
| aio_username | Your username for your io.adafruit.com account |
| aio_key      | Your API key for your io.adafruit.com account |
| timezone     | Your local timezone (see http://worldtimeapi.org/timezones) |

#### OpenWeather Credentials and Settings

This project uses the OpenWeather API to get current weather and forecast information. For the basic functionality that this project uses, a free account is sufficient. You can set that up at https://openweathermap.org/api.

| Secret Name       | Secret Description |
| ----------------- | ------------------ |
| openweather_token | Your openweather API token |
| latitude          | Your local latitude value |
| longitude         | Your local longitude value |
