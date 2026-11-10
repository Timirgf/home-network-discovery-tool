# Home Network Discovery and Inventory Tool

## Project Overview

I developed a Python-based home network discovery tool that uses Nmap to identify active devices on a local network.

The tool collects available device information, including IPv4 addresses, hostnames, MAC addresses, and manufacturer details. It then displays the results in the terminal and exports the inventory into a CSV file for documentation.

## Project Objectives

- Identify devices responding to network discovery probes.
- Retrieve available IP address and hostname information.
- Extract MAC addresses and manufacturer details when available.
- Automate network discovery using Python.
- Export discovered device information into a spreadsheet.

## Technologies Used

- Python 3
- Nmap
- XML parsing (`xml.etree.ElementTree`)
- CSV module
- macOS Terminal

## How It Works

1. Python executes an Nmap host discovery scan against my authorized home network.
2. Nmap returns the results in XML format.
3. Python parses the XML data.
4. The program extracts available device information.
5. The results are displayed in the terminal.
6. The discovered inventory is exported to a CSV file.

## Features

- Local network host discovery using Nmap's `-sn` option.
- IPv4 address extraction.
- Hostname resolution when available.
- MAC address and manufacturer extraction when available.
- Automatic CSV inventory generation.

## What I Learned

Through this project, I gained practical experience with:

- Python automation.
- Network discovery and IP addressing.
- Using Nmap for host discovery.
- Reading and processing XML output.
- Working with MAC addresses and manufacturer information.
- Exporting network inventory data into CSV format.
- Troubleshooting device discovery limitations.

## Project Screenshots

### Network Discovery Results
Add your terminal scan screenshot here.

### Python Program
Add a screenshot of your Python code here.

### CSV Network Inventory
Add a screenshot of the generated spreadsheet here.

## Testing Environment

This project was tested on my own authorized home network.

**Note:** Network discovery does not guarantee that every connected device will be detected. Devices that do not respond to discovery probes may not appear in the results. MAC addresses and manufacturer details may also be unavailable.

## Future Improvements

- Add device identification labels.
- Compare current scans with previous inventory records.
- Identify newly discovered devices.
- Add a simple graphical interface.

