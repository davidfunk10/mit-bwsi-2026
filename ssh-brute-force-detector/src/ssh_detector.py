# src/ssh_detector.py

import re
from collections import Counter
import argparse

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"
)

def parse_failed_logins(file_path):
    failed_attempts = Counter()
    ip_usernames = {}
    with open(file_path, "r") as file:
        for line in file:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                username = match.group(1)
                ip_address = match.group(2)
                failed_attempts[ip_address] += 1
                if ip_address not in ip_usernames:
                    ip_usernames[ip_address] = set()
                ip_usernames[ip_address].add(username)
               

    return failed_attempts, ip_usernames

def print_report(failed_attempts, ip_usernames, threshold):
    print("--------------------------------")
    print("SSH Brute Force Detection Report")
    print("--------------------------------")

    if not failed_attempts:
        print("No failed SSH login attempts found.")
        return

    for ip, count in failed_attempts.most_common():
        if count>= threshold:
            status = "Suspicious"
        else:
            status = "OK"

        print(f"{ip}: {count} failed attempts")
        print(f"  Status: {status}")
        print(f"  Usernames attempted: {', '.join(sorted(ip_usernames.get(ip, set())))}")
        if len(ip_usernames.get(ip, set())) >= 3:
            print("  ALERT: Multiple usernames targeted. Possible brute-force attack.")

def main():
    parser = argparse.ArgumentParser(description="Detect possible SSH brute-force attempts from Linux auth logs.")
    parser.add_argument("log_file", help="Path to the auth log file")
    parser.add_argument("--threshold", type=int, default=5, help="Failed login count needed to mark an IP as suspicious")

    args = parser.parse_args()

    failed_attempts, ip_usernames = parse_failed_logins(args.log_file)
    print_report(failed_attempts, ip_usernames, args.threshold)

if __name__ == "__main__":
    main()