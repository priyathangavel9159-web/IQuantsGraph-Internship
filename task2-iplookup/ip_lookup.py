
import requests
import csv
import logging
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


logging.basicConfig(
    filename=BASE_DIR / "ip_lookup.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)


def read_ips():
    file_path = BASE_DIR / "ips.txt"

    with open(file_path, "r") as file:
        ips = [line.strip() for line in file if line.strip()]

    return ips



def get_city(ip):
    url = f"https://ipinfo.io/{ip}/geo"

    try:
        response = requests.get(url, timeout=10)

        status = response.status_code

        
        if status != 200:
            logging.error(
                f"IP: {ip} | Status: {status} | Error: HTTP request failed"
            )
            return "Unknown"

       
        result = response.json()

       
        city = result.get("city")

        if not city:
            logging.warning(
                f"IP: {ip} | Status: {status} | Error: City not found"
            )
            return "Unknown"

        logging.info(
            f"IP: {ip} | Status: {status} | City: {city}"
        )

        return city

    except requests.exceptions.Timeout:
        logging.error(
            f"IP: {ip} | Status: N/A | Error: Request timed out"
        )
        return "Unknown"

    except requests.exceptions.RequestException as error:
        logging.error(
            f"IP: {ip} | Status: N/A | Error: {error}"
        )
        return "Unknown"

    except ValueError as error:
        logging.error(
            f"IP: {ip} | Status: {status} | Error: Invalid JSON - {error}"
        )
        return "Unknown"


def save_to_csv(results):
    file_path = BASE_DIR / "ip_locations.csv"

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ip", "city"])
        writer.writerows(results)



def main():
    ips = read_ips()

    results = []

    for ip in ips:
        city = get_city(ip)

        results.append([ip, city])

        print(f"{ip} : {city}")

    save_to_csv(results)

    print("\nCSV file created successfully!")
    print("Log file created successfully!")



if __name__ == "__main__":
    main()
