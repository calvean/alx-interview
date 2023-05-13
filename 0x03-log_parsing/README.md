Log Parsing

This script reads the standard input line by line, parses log lines, and computes various metrics such as the total file size and the count of each HTTP status code.
Requirements

    Python 3.x

Usage

    Open a terminal and navigate to the directory where the script is located.
    Run the script using the following command: python3 log_parsing.py < access.log
    The script will start reading the standard input and print file stats every 10 loops.
    To stop the script, press Ctrl+C.

Input

The script expects to read log lines from the standard input. The log lines should be in the following format:

<IP_ADDRESS> - [<DATE>] "<REQUEST>" <STATUS> <SIZE>

For example:

10.0.0.2 - - [07/Mar/2004:16:05:49 -0800] "GET /favicon.ico HTTP/1.1" 404 133

Output

The script prints the following metrics:

    File size: the total size of the log file in bytes
    Status codes: the count of each HTTP status code (200, 301, 400, 401, 403, 404, 405, 500)

The metrics are printed every 10 loops.
