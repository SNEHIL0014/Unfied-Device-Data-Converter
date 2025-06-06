import json
import unittest
import datetime

# Load JSON files
with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


# Helper to convert ISO8601 timestamp to milliseconds
def iso_to_millis(iso_str):
    dt = datetime.datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# Format 1 Conversion Function
def convertFromFormat1(jsonObject):
    # Step 1: Parse location
    location_parts = jsonObject.get("location", "").split("/")
    location = {
        "country": location_parts[0] if len(location_parts) > 0 else "",
        "city": location_parts[1] if len(location_parts) > 1 else "",
        "area": location_parts[2] if len(location_parts) > 2 else "",
        "factory": location_parts[3] if len(location_parts) > 3 else "",
        "section": location_parts[4] if len(location_parts) > 4 else "",
    }

    # Step 2: Map keys to expected structure
    result = {
        "deviceID": jsonObject.get("deviceID"),
        "deviceType": jsonObject.get("deviceType"),
        "timestamp": jsonObject.get("timestamp"),  # already in ms
        "location": location,
        "data": {
            "status": jsonObject.get("operationStatus"),
            "temperature": jsonObject.get("temp")
        }
    }
    return result


# Format 2 Conversion Function
def convertFromFormat2(jsonObject):
    # Step 1: Flatten device & convert timestamp
    timestamp_ms = iso_to_millis(jsonObject.get("timestamp"))

    # Step 2: Build result
    result = {
        "deviceID": jsonObject.get("device", {}).get("id"),
        "deviceType": jsonObject.get("device", {}).get("type"),
        "timestamp": timestamp_ms,
        "location": {
            "country": jsonObject.get("country"),
            "city": jsonObject.get("city"),
            "area": jsonObject.get("area"),
            "factory": jsonObject.get("factory"),
            "section": jsonObject.get("section")
        },
        "data": jsonObject.get("data")
    }
    return result


# Routing logic to choose the correct converter
def main(jsonObject):
    if jsonObject.get("device") is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


# Test Suite
class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, "Converting from Type 1 failed")

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, "Converting from Type 2 failed")


if __name__ == "__main__":
    unittest.main()


# This script converts two formats of device data into a standard JSON structure.
# Format 1: Flat data with a string-based location and timestamp in ms
# Format 2: Nested structure with ISO8601 timestamp
# All test cases pass successfully.
