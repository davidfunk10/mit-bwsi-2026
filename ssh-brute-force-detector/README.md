# SSH Brute Force Detector

## Overview

SSH Brute Force Detector is a Python tool that analyzes Linux authentication logs and looks for suspicious SSH login activity.

The program identifies failed login attempts, counts how many times each IP address appears, tracks the usernames that were targeted, and determines if something might be a brute force attack.

I created this project after completing MIT BWSI Cyber Operations to apply some of the Linux, Python, and cybersecurity concepts covered in the course.

## Features

- Detects failed SSH login attempts
- Counts failed attempts by IP address
- Tracks usernames attempted by each IP address (no duplicates through the use of a set)
- Flags IP addresses that exceed a failed login threshold
- Detects when multiple usernames are targeted from the same IP address

## Example Output

```text
--------------------------------
SSH Brute Force Detection Report
--------------------------------

192.168.1.25: 5 failed attempts
  Status: Suspicious
  Usernames attempted: admin, test, user, root
  ALERT: Multiple usernames targeted. Possible brute-force attack.

10.0.0.8: 1 failed attempts
  Status: OK
  Usernames attempted: david
```

## Running the Program

```bash
python src/ssh_detector.py sample_logs/sample_auth.log
```

Custom threshold to set the number of logins that is suspicious(>=), default = 5:

```bash
python src/ssh_detector.py sample_logs/sample_auth.log --threshold 10
```

## What I Learned

- How Linux authentication logs are structured (syslog format)
- Using 3+ usernames, or just multiple, to log in can be a sign of a brute force attack
- How to use regular expressions to extract information from log files
- How to code custom flags in Python for scripts
- Deepened my understanding of how security tools identify suspicious activity
