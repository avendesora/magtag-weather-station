import board
import busio
import adafruit_bme680
import adafruit_sgp30

i2c = busio.I2C(board.SCL, board.SDA)

# AdaFruit BME688
bme680_sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

print(
    f"Temperature: {bme680_sensor.temperature:.2f} C, Altitude: {bme680_sensor.altitude:.2f}"
)
print(f"Gas: {bme680_sensor.gas:.2f} ohms, Humidity: {bme680_sensor.humidity:.2f}%")
print(
    f"Pressure: {bme680_sensor.pressure:.2f} hPa, Rel. Humidity: {bme680_sensor.relative_humidity:.2f}%"
)
print(f"Sea Lvl Pressure: {bme680_sensor.sea_level_pressure:.2f}")

# AdaFruit SGP30
sgp30_sensor = adafruit_sgp30.Adafruit_SGP30(i2c)

print(
    f"eCO2: {sgp30_sensor.eCO2}ppm, base: {sgp30_sensor.baseline_eCO2}, "
    f"TVOC: {sgp30_sensor.TVOC}ppb, base: {sgp30_sensor.baseline_TVOC}"
)
print(f"Ethanol: {sgp30_sensor.Ethanol}")
