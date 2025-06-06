# Unified Device Data Converter

This is a Python utility for normalizing telemetry data from heterogeneous IoT devices into a unified JSON format. This tool helps standardize data structures from different device formats, enabling seamless integration with analytics or downstream processing pipelines.

---

## ✨ Features

- Converts data from **Format 1 (flat)** and **Format 2 (nested)** into a consistent unified format  
- Parses and restructures complex location strings into structured dictionaries  
- Converts timestamps, including ISO 8601 strings, into milliseconds since epoch  
- Normalizes device metadata and sensor data fields  
- Includes unit tests to verify correctness for both input formats  

---

✅ Testing
The project includes unit tests (using unittest) that validate:

Correctness of the expected output

Conversion logic from Format 1

Conversion logic from Format 2


📦 Requirements
Python 3.x

No external dependencies

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgments
Thanks to the original Replit project structure used as a foundation.

Feel free to open issues or submit pull requests to improve this project!


