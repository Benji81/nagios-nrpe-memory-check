#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='Check memory usage for Nagios')
parser.add_argument('-w', '--warning', type=int, default='70',
                    help='warning threshold. Between 0 and 100. Default: 70')
parser.add_argument('-c', '--critical', type=int, default='90',
                    help='critical threshold. Between 0 and 100. Default: 90')


if __name__ == '__main__':
    args = parser.parse_args()
    values = {}
    try:
        fd = open('/proc/meminfo')
        for line in fd.readlines():
            line = line.strip()
            match = re.match(r'''([^:]+):\s*(\d+) kB''', line)
            if match:
                values[match.group(1)] = match.group(2)
        available = int(values['MemAvailable'])
        total = int(values['MemTotal'])
        ratio = 100 * available / total
        if ratio >= args.warning:
            return_code = 1
            message = 'MEMORY WARNING'
        elif ratio >= args.critical:
            return_code = 2
            message = 'MEMORY CRITICAL'
        else:
            return_code = 0
            message = 'MEMORY OK'
        print('''%s - %dM available (%d%%) | 'available'=%dMB;;;%d;%d''' % (
            message,
            available / 1024,
            ratio,
            available / 1024,
            0,
            total / 1024)
              )
        sys.exit(return_code)
    except Exception as e:
        print(e)
        sys.exit(3)
