#!/usr/bin/python3

import sys

def print_stats(total_size, status_codes):
    """Print file size and number of lines by status code."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def parse_line(line):
    """Parse a log line and extract relevant information."""
    try:
        parts = line.split(" ")
        size = int(parts[-1])
        code = int(parts[-2])
        return size, code
    except (ValueError, IndexError):
        return None, None

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            size, code = parse_line(line.strip())
            
            if size is not None and code in status_codes:
                total_size += size
                status_codes[code] += 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass  # Handle KeyboardInterrupt to print final stats

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

