

import subprocess
import xml.etree.ElementTree as ET
import csv
from pathlib import Path

# =====================================
# HOME NETWORK DISCOVERY TOOL
# =====================================

# Your home network range
network = "192.168.1.0/24"

# CSV file location: same folder as this script
filename = Path(__file__).resolve().parent / "network_inventory.csv"

print("\n===================================")
print("       HOME NETWORK DISCOVERY")
print("===================================")
print("Scanning network:", network)
print("\nPlease wait...\n")

try:
    # Run Nmap host discovery only
    result = subprocess.run(
        [
            "sudo",
            "nmap",
            "-sn",
            "-R",
            "--reason",
            "-oX",
            "-",
            network
        ],
        capture_output=True,
        text=True,
        timeout=120
    )

    # Check for Nmap errors
    if result.returncode != 0:
        print("Nmap error:")
        print(result.stderr)

    else:
        # Convert Nmap XML output into Python data
        root = ET.fromstring(result.stdout)

        devices = []

        print("========== NETWORK INVENTORY ==========")

        print(
            f"{'IP ADDRESS':<18}"
            f"{'HOSTNAME':<25}"
            f"{'MAC ADDRESS':<20}"
            f"{'MANUFACTURER':<20}"
        )

        print("-" * 83)

        # Examine every discovered host
        for host in root.findall("host"):

            # Check whether the device is up
            status = host.find("status")

            if status is None or status.get("state") != "up":
                continue

            # Get IPv4 address
            address = host.find(
                "address[@addrtype='ipv4']"
            )

            if address is None:
                continue

            ip_address = address.get("addr")

            # Get hostname
            hostname_element = host.find(
                "hostnames/hostname"
            )

            if hostname_element is not None:
                hostname = hostname_element.get("name")
            else:
                hostname = "Unknown"

            # Get MAC address and manufacturer
            mac_element = host.find(
                "address[@addrtype='mac']"
            )

            if mac_element is not None:
                mac_address = mac_element.get("addr")
                manufacturer = mac_element.get(
                    "vendor", "Unknown"
                )
            else:
                mac_address = "Unknown"
                manufacturer = "Unknown"

            # Display device information
            print(
                f"{ip_address:<18}"
                f"{hostname:<25}"
                f"{mac_address:<20}"
                f"{manufacturer:<20}"
            )

            # Store information for CSV export
            devices.append({
                "IP Address": ip_address,
                "Hostname": hostname,
                "MAC Address": mac_address,
                "Manufacturer": manufacturer
            })

        # Display total devices
        print("-" * 83)
        print("Total devices discovered:", len(devices))

        # Export results to CSV
        with filename.open(
            mode="w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            fieldnames = [
                "IP Address",
                "Hostname",
                "MAC Address",
                "Manufacturer"
            ]

            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(devices)

        print("\n===================================")
        print("NETWORK INVENTORY SAVED!")
        print("File:", filename)
        print("===================================")

except subprocess.TimeoutExpired:
    print("The network scan timed out.")

except FileNotFoundError:
    print("Nmap could not be found. Check your installation.")

except ET.ParseError:
    print("Unable to read Nmap XML results.")

except PermissionError:
    print("Permission denied while saving the CSV file.")

except KeyboardInterrupt:
    print("\nNetwork discovery interrupted.")

except Exception as error:
    print("An unexpected error occurred:")
    print(error)
