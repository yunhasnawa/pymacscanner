#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

import subprocess

from MacParser import MacParser


class MacScanner:

    def __init__(self, endpoint: str, ip_range='192.168.1.0/24'):
        self.endpoint = endpoint
        self.ip_range = ip_range
        self.scan_result = None
        self.upload_result = ''

    @staticmethod
    def create_runner(command: str):
        print("Executing: {}".format(command))
        runner = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        return runner

    def scan(self) -> int:
        cmd = 'nmap -sP -n {0}'.format(self.ip_range)
        runner = MacScanner.create_runner(cmd)
        parser = MacParser()
        for line in runner.stdout.readlines():
            parser.parse_nmap_output_line(str(line))
        self.scan_result = parser.get_scan_result()
        return runner.wait()  # Result = 0 -> Success

    def upload(self):
        if self.scan_result is None:
            return '[ERR] Result is empty!'
        json = self.scan_result.to_json()
        cmd = ('curl -d ' +
               "'{0}'".format(json) +
               ' -H "Content-Type: application/json" -X POST {0}'.format(self.endpoint))
        runner = MacScanner.create_runner(cmd)
        out = runner.stdout.readlines()
        response = out[(len(out) - 1)]
        self.upload_result = str(response)
        return runner.wait()  # Result = 0 -> Success
