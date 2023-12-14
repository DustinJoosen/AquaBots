import platform


def get_moisture(pin=2, verbose=False):
    if verbose:
        print("Importing required modules")

    try:
        from grove.grove_moisture_sensor import GroveMoistureSensor
    except ModuleNotFoundError:
        print("Sensor can only be read on a linux-based operating system")
        return -1

    if verbose:
        print(f"Starting moisture detection on pin {pin}")

    sensor = GroveMoistureSensor(pin)

    if verbose:
        print("Detecting moisture")

    moisture = sensor.moisture

    if verbose:
        print(f"Moisture detected: {moisture}")

    return moisture


def main():
    moisture = get_moisture(pin=2, verbose=True)

    if 0 <= moisture and moisture > 300:
        result = "Dry"
    elif 300 <= moisture and moisture > 600:
        result = "Moist"
    else:
        result = "Wet"

    print(f"{result} ({moisture})")


if __name__ == "__main__":
    if not platform.system() == "Linux":
        raise SystemError("Sensor can only be read on a linux-based operating system")

    main()
