#!/usr/bin/python3
"""
0. Log parsing task's module.
"""

import sys


def print_statistics(status_codes, total_size):
    """
    Prints the accumulated statistics of file
    size and status code counts.

    Args:
        status_codes (dict): A dictionary with status
        codes as keys and counts as values.
        total_size (int): The total file size processed.

    Returns:
        None
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


total_file_size = 0
line_count = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


try:
    for line in sys.stdin:
        # Split and reverse the line for easier extraction
        parts = line.split()[::-1]

        if len(parts) < 2:
            continue

        try:
            file_size = int(parts[0])
            status_code = parts[1]

            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1
            if line_count == 10:
                print_statistics(status_code_counts, total_file_size)
                line_count = 0

        except ValueError:
            continue


except KeyboardInterrupt:
    pass

print_statistics(status_code_counts, total_file_size)
