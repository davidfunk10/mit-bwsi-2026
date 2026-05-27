# src/ssh_detector.py

import re
from collections import Counter
import argparse

FAILED_LOGIN_PATTERN = re.compile(r"Failed password.* from (\d+\.\d+\.\d+\.\d+)")

def parse_failed_logins(file_path):
    failed_attempts = Counter()

    with open(file_path, "r") as file:
        for line in file:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                ip_address = match.group(1)
                failed_attempts[ip_address] += 1

    return failed_attempts

def print_report(failed_attempts, threshold):
    print("SSH Brute Force Detection Report")
    print("--------------------------------")

    if not failed_attempts:
        print("No failed SSH login attempts found.")
        return

    for ip, count in failed_attempts.most_common():
        status = "SUSPICIOUS" if count >= threshold else "normal"
        print(f"{ip}: {count} failed attempts - {status}")

def main():
    parser = argparse.ArgumentParser(description="Detect possible SSH brute-force attempts from Linux auth logs.")
    parser.add_argument("log_file", help="Path to the auth log file")
    parser.add_argument("--threshold", type=int, default=5, help="Failed login count needed to mark an IP as suspicious")

    args = parser.parse_args()

    failed_attempts = parse_failed_logins(args.log_file)
    print_report(failed_attempts, args.threshold)

if __name__ == "__main__":
    main()