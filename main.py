#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

from MacScanner import MacScanner

scanner: MacScanner


def setup():
    endpoint = 'https://your/endpoint/url'
    ip_range = '192.168.1.0/24'
    global scanner
    scanner = MacScanner(endpoint, ip_range)


def loop():
    scan_output = scanner.scan()
    if scan_output == 0:
        upload_output = scanner.upload()
        if upload_output == 0:
            print(scanner.upload_result)
        else:
            print("[ERROR] Upload failed!")
    else:
        print("[ERROR] Scan failed!")
    wait(10000)


def wait(ms):
    import time
    print("Waiting for {} ms".format(ms))
    time.sleep(ms/1000)


def main():
    setup()
    while True:
        loop()


main()
