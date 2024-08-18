
#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

import datetime

from Config import Config
from ScanResult import ScanResult


class MacParser:

    def __init__(self):
        self.mac_addresses = []

    def parse_nmap_output_line(self, line: str):
        if "MAC Address: " in line:
            splits1 = line.split("MAC Address: ")
            if len(splits1) > 1:
                splits2 = splits1[1].split(" ")
                if len(splits2) > 1:
                    mac_addr = splits2[0]
                    self.mac_addresses.append(mac_addr)

    def get_scan_result(self) -> ScanResult:
        current_time = datetime.datetime.now()
        scanner_id = Config.instance().get('scanner_id')
        result = ScanResult(scanner_id, str(current_time), self.mac_addresses)
        return result
