#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys
from typing import Dict, List


def print_file_stats(file_size: int, status_codes: Dict[int, int]) -> None:
    """
    Function to print file size and stats every 10 loops
    Args:
        file_size - total size of file
        status_codes - dictionary of status codes with their counts
    Returns:
        None
    """
    print('File size: {}'.format(file_size))

    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print('{}: {}'.format(code, status_codes[code]))


def parse_log_line(
  line: str,
  file_size: List[int],
  status_codes: Dict[int, int]) -> None:
    """
    Function to parse a single line of log file
    Args:
        line - single line of log file
        file_size - total size of file
        status_codes - dictionary of status codes with their counts
    Returns:
        None
    """
    try:
        line = line.rstrip('\n')
        words = line.split(' ')
        file_size[0] += int(words[-1])
        status_code = int(words[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except (ValueError, IndexError):
        pass


if __name__ == "__main__":
    """ Log Parsing module """
    status_codes = {
      200: 0,
      301: 0,
      400: 0,
      401: 0,
      403: 0,
      404: 0,
      405: 0,
      500: 0}
    file_size = [0]
    count = 1

    try:
        for line in sys.stdin:
            parse_log_line(line, file_size, status_codes)
            if count % 10 == 0:
                print_file_stats(file_size[0], status_codes)
            count += 1
    except KeyboardInterrupt:
        print_file_stats(file_size[0], status_codes)
        raise
    print_file_stats(file_size[0], status_codes)
