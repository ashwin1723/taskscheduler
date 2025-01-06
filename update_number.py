#!/usr/bin/env python3
import os
import random
import time
from datetime import datetime

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    """Reads the number from number.txt or initializes it if missing."""
    if not os.path.exists('number.txt'):
        write_number(0)  # Initialize the file with 0 if it doesn't exist
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    """Writes the given number to number.txt."""
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit():
    """Commits the updated number.txt file."""
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os.system(f'git add number.txt')
    os.system(f'git commit -m "Update number: {date}"')

def git_push():
    """Pushes the committed changes to the repository."""
    os.system('git push')

def main():
    # Generate a random number of updates (2 to 4)
    updates_today = random.randint(2, 4)
    print(f"Number of updates today: {updates_today}")

    for i in range(updates_today):
        # Update the number
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)

        # Commit and push changes
        git_commit()
        git_push()
        print(f"Update {i + 1}/{updates_today} completed.")

        # Add a random delay between updates (e.g., 1-3 hours)
        if i < updates_today - 1:  # No delay after the last update
            delay = random.randint(3600, 10800)  # Delay in seconds (1 to 3 hours)
            print(f"Waiting for {delay // 3600} hours before the next update...")
            time.sleep(delay)

if __name__ == "__main__":
    main()
