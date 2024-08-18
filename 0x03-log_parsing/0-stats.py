#!/usr/bin/python3
"""Stats module"""
import sys
import re
from typing import Dict

status_obj = {}
total_file_size = 0
line_count = 0
status_code_array = [200, 301, 400, 401, 403, 404, 405, 500]

pattern = (
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    + r'\[([\d-]+\s[\d:.]+)\] "GET /projects/260 HTTP/1.1" '
    + r"(?P<status_code>\d{3}) (?P<file_size>\d+)"
)


def print_stats(total_file_size: int, status_code_obj: Dict[int, int]) -> None:
    """print_stats- prints the statistics

    Args:
        total_file_size (int): total file size
        status_code_obj (Dict[int, int]): status code objects
    """
    print(f"File size: {total_file_size}")
    for key in sorted(status_code_obj.keys()):
        print(f"{key}: {status_code_obj[key]}")
    sys.stdout.flush()


try:
    for line in sys.stdin:
        line_count += 1
        match = re.match(pattern, line)

        if match:
            status_code = match.group("status_code")
            file_size = match.group("file_size")
            file_size = int(file_size)

            try:
                status_code = int(status_code)
            except ValueError:
                status_code = ""

            if status_code in status_code_array:
                total_file_size += file_size
                status_obj[status_code] = status_obj.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_stats(total_file_size, status_obj)

finally:
    print_stats(total_file_size, status_obj)
