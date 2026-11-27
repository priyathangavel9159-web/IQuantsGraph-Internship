Task 2 – IP Geolocation and Logging

Project Description
This task retrieves geographical information for IP addresses using the IPinfo API. It extracts the city name for each IP address and stores the results in a CSV file. Logging is used to record successful requests and errors.

Technologies Used
- Python
- Requests
- CSV
- Logging
- pathlib

Features
- Reads IP addresses from `ips.txt`.
- Sends HTTP GET requests to the IPinfo API.
- Retrieves city information for each IP address.
- Handles HTTP errors, timeouts and missing city information.
- Displays `Unknown` when city information is unavailable.
- Stores IP addresses and corresponding cities in `ip_locations.csv`.
- Records timestamps, IP addresses, statuses and errors in `ip_lookup.log`.

Installation
Install the required package using:

   pip install -r requirements.txt


The `requirements.txt` file contains:

requests


How to Run
1. Open the task2-iplookup folder in VS Code.
2. Ensure that `ips.txt` contains the IP addresses.
3. Open the terminal.
4. Run the following command:
      python ip_lookup.py

Expected Output
The program displays the IP addresses and their corresponding city names.

Example:


121.127.64.72 : City name
162.43.143.200 : City name

Actual city results depend on the API response.

Output Files
- `ip_locations.csv` – Stores IP addresses and city names.
- `ip_lookup.log` – Stores execution logs and error information.

Project Files
- `ip_lookup.py` – Python source code.
- `ips.txt` – Input IP addresses.
- `requirements.txt` – Required Python package.
- `ip_locations.csv` – Generated CSV file.
- `ip_lookup.log` – Generated log file.
- `README.md` – Project documentation.

Conclusion
This task demonstrates API integration, HTTP requests, JSON processing, CSV file handling and logging in Python.