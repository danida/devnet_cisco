from dotenv import load_dotenv
from requests import request


class Scanning_API:
    def __init__(self):
        self.config = load_dotenv(dotenv_path='.env')

    def get_locationJSON(self):
        global locationdata
        secret = "asd"
        version = 2
        if not request.json or not "data" in request.json:
            return ("invalid data", 400)

        locationdata = request.json
        print(locationdata, indent=1)
        print("Received POST from ", request.environ["REMOTE_ADDR"])

        # Verify secret
        if locationdata["secret"] != secret:
            print("secret invalid:", locationdata["secret"])
            return ("invalid secret", 403)

        else:
            print("secret verified: ", locationdata["secret"])

        if locationdata["version"] != version:
            print("invalid version")
            return ("invalid version", 400)

        # else:
        #     print("version verified: ", locationdata["version"])

        # Determine device type
        if locationdata["type"] == "DevicesSeen":
            print("WiFi Devices Seen")
        elif locationdata["type"] == "BluetoothDevicesSeen":
            print("Bluetooth Devices Seen")
        else:
            print("Unknown Device 'type'")
            return ("invalid device type", 403)

        # Return success message
        return "Location Scanning POST Received"