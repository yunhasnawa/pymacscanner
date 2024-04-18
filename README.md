# pymacscanner
Python MAC address scanner using NMAP.

---

## Description
This script will scan MAC addresses of devices connected in the same network then sends the results in JSON format to a specific endpoint using HTTP POST method.

Sample results:
```json
{
  "scannerId": "1",
  "scanTime": "2024-04-18 20:47:39.622043",
  "macAddresses": [
    "1A:2B:3C:4D:5E:6A",
    "1A:2B:3C:4D:5E:6B",
    "1A:2B:3C:4D:5E:6C"
  ]
}
```

## Requirements
The following software must be installed on your system and registered in its environment variables:
1. Python >= 3.7
2. Nmap (https://nmap.org)
3. curl (https://curl.se)

## Usage
1. In `main.py`, specify the IP range and the URL to send the scan results.
   ```python
   def setup():
    endpoint = 'https://your/endpoint/url'
    ip_range = '192.168.1.0/24'
    global scanner
    scanner = MacScanner(endpoint, ip_range)
   ```
   
2. Execute the script:
   ```shell
   $sudo python3 main.py
   ```

---   

### Legal Note
This script was written for educational and private use only. I do not assume liability for any kind of functioning or legal compliance of its application.