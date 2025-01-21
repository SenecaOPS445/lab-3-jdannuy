#!/usr/bin/env python3

# Author ID:  Jhanlyn Brita Dannuy
import subprocess

def free_space():
    # Run the command to get free disk space on the root directory
    result = subprocess.run(
        ["df", "-h", "--output=avail", "/"],
        capture_output=True,
        text=True
    )
    # Extract the output, skipping the header row, and return stripped output
    return result.stdout.splitlines()[1].strip()

if __name__ == "__main__":
    print(free_space())
