#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

class ScanResult:

    def __init__(self, scanner_id: str, scan_time: str, mac_addresses: list):
        self.scanner_id = scanner_id
        self.scan_time = scan_time
        self.mac_addresses = mac_addresses

    def to_json(self) -> str:
        return ('{'
                '"scannerId":"' + self.scanner_id + '", '
                '"scanTime": "' + self.scan_time + '", '
                '"macAddresses": ' + (self.serialized_mac_addresses()) + '}')

    def serialized_mac_addresses(self) -> str:
        count = 0
        serialized = '['
        for addr in self.mac_addresses:
            serialized += '"' + addr + '"'
            count += 1
            if count < len(self.mac_addresses):
                serialized += ', '
        serialized += ']'
        return serialized
